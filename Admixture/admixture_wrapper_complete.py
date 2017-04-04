import sys
import os
import subprocess as sp
import shutil
from datetime import datetime
import numpy as np
'''
admixture_wrapper_complete.py [directory with ped and map files ("recoded 12" ped files)]

Will run program admixture on a directory of ped files, each assumed to have
a unique prefix. User selects range of K values and number of replicates
per K. The Q, P, and log files are written to a directory with the same
name as the prefix of each ped file. After completing analyses for a
ped file, the log files will be summarized to obtain the cross-validation
error values for each replicate per K, and an average and SD will be
calculated which can be easily plotted with the associated R script.

##############
DEPENDENCIES:
admixture - requires to be in path
numpy
##############

------------------------
written for Python 2.7
Dan Portik
daniel.portik@uta.edu
March 2017
------------------------
'''
t_begin = datetime.now()

target_directory = sys.argv[1]
os.chdir(target_directory)

all_files = []
for filetype in os.listdir('.'):
    if filetype.endswith('.ped'):
        all_files.append(filetype)
                
file_no = len(all_files)

print
print "-----------------------------------------------------------------------------------------------------"
print "There are {} ped files in the current directory.".format(file_no)
print "-----------------------------------------------------------------------------------------------------"
print

decision_k = None
while decision_k is None:
    try:
        decision_k = 1 + int(raw_input("Select upper range of K value to analyze per file: "))
    except ValueError:
        print "That wasn't a number."
print '\n','\n'

decision_r = None
while decision_r is None:
    try:
        decision_r = 1 + int(raw_input("Select number of replicates to run per K: "))
    except ValueError:
        print "That wasn't a number."
print '\n','\n'


for ped in all_files:
    ped_name = ped.split('.')
    out_dir = ped_name[0]+'_Outputs'
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    for i in range(1,decision_k):
        for rep in range(1,decision_r):
            t0 = datetime.now()
            call_string = "admixture {0} {1} -j2 --cv=10 | tee {2}.{1}.log.out".format(ped, i, ped_name[0])
            proc_admx = sp.call(call_string, shell=True)
            t1 = datetime.now()
            total_t = t1 - t0
            print '\n', '\n', "-----------------------------------------------------------------------------------------------------"
            print "Finished analysis"
            print "Total time for {3} K={0} replicate {1}: {2} (H:M:S)".format(i,rep,total_t,ped_name[0])
            print "-----------------------------------------------------------------------------------------------------", '\n', '\n'
            for filetype in os.listdir('.'):
                if filetype.startswith(ped_name[0]):
                    if filetype.endswith('.P') or filetype.endswith('.Q') or filetype.endswith('.out'):
                        move_name = out_dir+"/"+filetype+".rep{}".format(rep)
                        shutil.move(filetype, move_name)


    os.chdir(out_dir)
    k_number = set()
    for filetype in os.listdir('.'):
        bits = filetype.split('.')
        if len(bits) >= 3:
            #Clade1_fixed.1.log.out.rep4
            k_number.add(bits[1])
            prefix = bits[0]

    k_number = list(k_number)
    k_number.sort(key=int)

    out_name = prefix+"_cross_validation_all_outputs.txt"
    fh_out1 = open(out_name, 'a')
    fh_out1.write("K_Value\tRep\tValue\n")

    out_name = prefix+"_cross_validation_averages.txt"
    fh_out2 = open(out_name, 'a')
    fh_out2.write("K\tCV_avg\tCV_sd\n")

    for k in k_number:
        cv_list = []
        for filetype in os.listdir('.'):
            bits = filetype.split('.')
            if len(bits) >= 3:
                if bits[1] == k and bits[2] == "log":
                    fh_temp = open(filetype, 'r')
                    lines = fh_temp.readlines()
                    for line in lines:
                        if line.startswith("CV error"):
                            line = line.strip()
                            line = line.split(': ')
                            cv_val = line[1]
                            cv_list.append(cv_val)
                    fh_out1.write("{0}\t{1}\t{2}\n".format(bits[1], bits[4], cv_val))
                    fh_temp.close()

        cv_array = np.asarray(cv_list,dtype=np.float64)
        cv_av = np.average(cv_array)
        cv_av = np.around(cv_av, decimals = 4)
        cv_sd = np.std(cv_array,dtype=np.float64)
        cv_sd = np.around(cv_sd, decimals = 4)
        fh_out2.write("{0}\t{1}\t{2}\n".format(k, cv_av, cv_sd))

    fh_out1.close()
    fh_out2.close()

    os.chdir(target_directory)
                
t_finish = datetime.now()
elapsed = t_finish - t_begin

print '\n', '\n', "-----------------------------------------------------------------------------------------------------"
print "Finished all analyses!"
print "Total time: {0} (H:M:S)".format(elapsed)
print "-----------------------------------------------------------------------------------------------------", '\n', '\n'
