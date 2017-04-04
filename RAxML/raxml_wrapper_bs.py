import sys
import os
import subprocess as sp
import shutil

''''
Usage: python raxml_wrapper.py [directory with all 'Contig.phylip' or 'Contig.phy' files]

example: python dan/scripts/raxml_wrapper.py dan/exons/phylip_files

-Will run search directory for "NAME.phylip" files and the give option to execute raxml.
Moves best tree files with '.tre' extension added to output folder '/Best_trees'
Moves all other files from each run to '/Raxml_files'
Check these folders for progress.


-Uses the following default command string to execute raxml:

raxmlHPC -m GTRCAT -p 12345

-You can edit this in RAXML_string below. Change the settings you want,
but the input and output are automated so leave these strings out (-s, -n).
Add or change the analysis type here, using the syntax and flags of raxml.
If not running raxmlHPC, change program name below too.
KEEP the quotations around the string or the script will crash.
'''
#######################################################################################
RAXML_string = "raxmlHPC -f a -m GTRCAT -p 12345 -x 12345 -# 500"
#######################################################################################
'''
Examples of other useful command strings:
     "raxmlHPC -m GTRCAT -p 12345" -----basic run for best tree
     "raxmlHPC -m GTRCAT -p 12345 -# 20" -----for multiple (20) runs per file
     "raxmlHPC -f a -m GTRCAT -p 12345 -x 12345 -# 100" ----for rapid bootstrapping (100 reps) and best ml tree
     "raxmlHPC -x 12345 -p 12345 -# autoMRE -m GTRCAT" ----for  high auto stop rapid bootstrapping (up to 1000 reps) and best ml tree


##############
DEPENDENCIES:
raxml - requires raxmlHPC to be in path (or another version like PTHREADS, in which case the string above needs to be changed)
##############

------------------------
written for Python 2.7.3
Dan Portik
daniel.portik@berkeley.edu
August 2015
------------------------
'''

fasta_directory = sys.argv[1]
os.chdir(fasta_directory)

all_files = []

for filetype in os.listdir('.'):
    if filetype.endswith('.phylip') or filetype.endswith('.phy'):
        all_files.append(filetype)
                
file_no = len(all_files)

print
print "-----------------------------------------------------------------------------------------------------"
print "There are {} phylip files in the current directory.".format(file_no)
print "-----------------------------------------------------------------------------------------------------"
print

analysis_decision = (raw_input("Would you like to analyze these files (y, n)? "))

if analysis_decision == 'n':
    print '\n', "No analyses will be performed, now quitting program.", '\n'
    
elif analysis_decision == 'y':

    #directory for best tree files
    out_dir = fasta_directory+'/'+'Best_trees'
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    #directory for all other raxml files for this session
    out_dir2 = fasta_directory+'/'+'Raxml_files'
    if not os.path.exists(out_dir2):
        os.mkdir(out_dir2)

    for phy in all_files:
            
            print "-----------------------------------------------------------------------------------------------------"
            print "Beginning raxml run of", phy
            print "-----------------------------------------------------------------------------------------------------"
            
            #split file name by the period in it
            phy_split = phy.split('.')
            #take the beginning of the file name to use to name our output file
            file_prefix = phy_split[0]
            #assign the file in this iteration to a variable to call
            input_f = phy
            #assign the prefix of the file in this iteration to a variable to call as output prefix
            output = file_prefix
            #create call string
            call_string = RAXML_string+" -s {0} -n {1}".format(input_f,output)
            #call command line for raxml with information above
            proc_raxml = sp.call(call_string, shell=True)

            print "-----------------------------------------------------------------------------------------------------"
            print "Finished raxml run of", phy
            print "-----------------------------------------------------------------------------------------------------"
            
            for filetype2 in os.listdir('.'):
                if filetype2.startswith('RAxML_bestTree'):
                    new_name = filetype2+'.tre'
                    new_file = out_dir+'/'+new_name
                    shutil.copyfile(filetype2, new_file)
                    print "-----------------------------------------------------------------------------------------------------"
                    print "Copied best tree of {0} to '/Best_Tree_files/{1}'".format(filetype2, new_name)
                    print "-----------------------------------------------------------------------------------------------------"
                if filetype2.startswith('RAxML_'):
                    proc = sp.Popen(['mv', filetype2, out_dir2])
                    proc.wait()
                if filetype2.endswith('.reduced'):
                    proc = sp.Popen(['mv', filetype2, out_dir2])
                    proc.wait()
    print
    print "*************************************************************************"
    print '\n', "All raxml runs finished!", '\n'
    print "*************************************************************************"
    print
else:
	print '\n', "Not a valid choice (y, n), now quitting program.", '\n'
