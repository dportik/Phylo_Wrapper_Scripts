import sys
'''
usage: python General_name_replacer.py [name change text file] [general file to change] 

Replace a set of names within a single file.

Name change file is a tab delimited text file with newline breaks at the end of each line (\n):
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

#get file to rename
file_name = sys.argv[2]
fh_file = open(file_name, 'r')

#make output file
out_name = file_name+"_Renamed"
fh_out = open(out_name, 'a')

#create dictionary for names and replacement values
name_dict = {}

#iterate through name file and populate dictionary
for line in fh_names:
    line = line.strip()
    line = line.split('\t')
    if len(line) > int(1):
        name_dict[line[0]]=line[1]

#Create a tuple out of the dictionary for sorting purposes
name_tuple = name_dict.items()
#sort the list by length of 'key' or first element (ie so biggest words get replaced first)
name_tuple = sorted(name_tuple, key=lambda x: len(x[0]), reverse=True)

#define function for searching and replacing
def Multiple_Replacer(string, tup):
    for originalname, replacename in tup:
        string = string.replace(originalname, replacename)
    return string

#iterate through file lines
for line in fh_file:
    line = line.strip()
    #execute function on each line
    replaceline = Multiple_Replacer(line, name_tuple)
    print "#########################################################################"
    print "-Replacing the following line:", '\n','\n', line, '\n'
    print "-With the updated line:", '\n','\n', replaceline, '\n'
    print "#########################################################################"
    #write replaced line to output file
    fh_out.write(replaceline+'\n')

fh_names.close()
fh_file.close()
fh_out.close()
