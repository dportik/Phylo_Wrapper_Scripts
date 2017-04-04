import sys
import os
import shutil
'''
usage: python General_name_replacer.py [name change text file] [directory with files to change] 

Replace a set of names in every file present in the target directory. 

Name change file is a tab delimited text file:
original_name1 new_name1
original_name2 new_name3

Will replace all names that match in input file and create an output file in the 
same directory with a '_Renamed' extension on it.

------------------------
written for Python 2.7
Dan Portik
daniel.portik@berkeley.edu
August 2015
------------------------
'''

#get name change file
name_list = sys.argv[1]
fh_names = open(name_list, 'r')
print '\n',"Opening name change key {}...".format(name_list),'\n'

#create dictionary for names and replacement values
name_dict = {}

#iterate through name file and populate dictionary
for line in fh_names:
    line = line.strip()
    line = line.split('\t')
    if len(line) > int(1):
        name_dict[line[0]]=line[1]
        print "Replace {} with {}...".format(line[0], line[1])

#Create a tuple out of the dictionary for sorting purposes
name_tuple = name_dict.items()
#sort the list by length of 'key' or first element (ie so biggest words get replaced first)
name_tuple = sorted(name_tuple, key=lambda x: len(x[0]), reverse=True)

#define function for searching and replacing
def Multiple_Replacer(string, tup):
    for originalname, replacename in tup:
        string = string.replace(originalname, replacename)
    return string


#====================================================================================
#execute function across all files in directory

#move to directory
file_dir = sys.argv[2]
os.chdir(file_dir)

for filetype in os.listdir('.'):
    if os.path.getsize(filetype) > int(0):
        print '\n', "***************************************************************", '\n', "Replacing contents in {}: ".format(filetype)

        fh_temp = open(filetype, 'r')

        #make output file
        out_name = "Renamed_"+filetype
        fh_out = open(out_name, 'a')

        #iterate through file lines
        for line in fh_temp:
            line = line.strip()
            #execute function on each line
            replaceline = Multiple_Replacer(line, name_tuple)
            #print '\t',"========================================================="
            #print '\t',"-Replacing line:"
            #print '\t','\t',line, '\n'
            #print '\t',"-With updated line:"
            #print '\t','\t',replaceline
            #print '\t',"========================================================="
            #write replaced line to output file
            fh_out.write(replaceline+'\n')

        fh_out.close()
        fh_temp.close()

out_dir = "Renaming_Output"
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

for filetype in os.listdir('.'):
    if filetype.startswith("Renamed_"):
        shutil.move(filetype, out_dir)
    
fh_names.close()
