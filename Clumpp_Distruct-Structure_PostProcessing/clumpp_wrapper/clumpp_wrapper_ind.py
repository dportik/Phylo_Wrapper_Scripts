import sys
import os
import subprocess as sp
import shutil
from datetime import datetime
''''
Usage: python clumpp_wrapper.py [directory with all clumpp indfiles]

Executes CLUMPP across a bin of 'K#.indfile' files, ideally resulting from
something like Structure Harvester.  Requires user input of number of individuals
and number of replicates per K, then executes across all indfiles automating
some necessary information.

The paramfile should also be in this directory. NOTE that not all commands in the
paramfile will be overwritten with command line arguments.  See bottom for commands 
able to be included, and check all remaining params in the file to ensure they 
are in fact correct.  

##############
DEPENDENCIES:
clumpp - requires clumpp executable in same directory as clumpp indfiles
##############
------------------------
written for Python 2.7
Dan Portik
daniel.portik@uta.edu
March 2016
------------------------
'''

clumpp_dir = sys.argv[1]
os.chdir(clumpp_dir)

print '\n','\n'
individuals = (raw_input("Number of individuals in data set: "))
runs = (raw_input("Number of replicates per K: "))


k_list = []


for filetype in os.listdir('.'):
    if filetype.startswith("K"):
        prefix = filetype.split('.')
        k_list.append(prefix[0][1:])
        
k_list.sort(key=int)

for K in k_list:
    t0 = datetime.now()
    print "********************************************************"
    print "{0}: Now beginning CLUMPP analysis of K = {1}...".format(datetime.now().strftime("%b-%d %H:%M"),K)
    print "********************************************************"
    indfile = "K{}.indfile".format(K)
    outfile = "K{}.indq".format(K)
    miscfile = "K{}.miscfile".format(K)
    

    clumpp_call = "./CLUMPP paramfile -i {0} -o {1} -j {2} -k {3} -c {4} -r {5} -m 2 -w 0 -s 2".format(indfile, outfile, miscfile, K, individuals, runs)
    proc_clumpp = sp.call(clumpp_call, shell=True)

    t1 = datetime.now()
    total_t = t1 - t0
    print "Total time: {}".format(total_t), '\n', '\n'
    
# Command line arguments for CLUMPP
# -i INDFILE
# -p POPFILE
# -o OUTFILE
# -j MISCFILE
# -k K
# -c C
# -r R
# -m M
# -w W
# -s S
