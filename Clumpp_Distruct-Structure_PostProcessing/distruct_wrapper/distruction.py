import sys
import os
import subprocess as sp
import shutil
import datetime
''''
Usage: python distruction.py [directory with all clumpp output files]

Reads K#.indq files in a directory. Makes a K#.popq file for each
to allow visualizing each individual as a separate, labeled bar.
Creates a drawparams file for each K for distruct, then creates
an output graphic for each K.

##############
DEPENDENCIES:
distruct
##############
------------------------
written for Python 2.7
Dan Portik
daniel.portik@uta.edu
March 2016
------------------------
'''

main_dir = sys.argv[1]
os.chdir(main_dir)

print '\n','\n'
inds = (raw_input("Number of individuals/pops in data set: "))

#Get K numbers from K#.indq files
k_list = []
for filetype in os.listdir('.'):
    if filetype.startswith("K"):
        prefix = filetype.split('.')
        k_list.append(prefix[0][1:])
k_list.sort(key=int)

def popq_maker():
    for filetype in os.listdir('.'):
        if filetype.endswith(".indq"):
            print '\n', "****************************************"
            print "Reading in {}".format(filetype)
            print "****************************************"

            prefix = filetype.split('.')

            temp_fh = open(filetype, 'r')
            lines = temp_fh.readlines()

            outname = prefix[0]+".popq"
            fh_out = open(outname, 'a')

            out_file_list = []

            for line in lines:
                line = line.strip()
                line_list = line.split()

                pop_ID = line_list[0]+':'

                fh_out.write(pop_ID+"   ")
                for item in line_list[5:]:
                    fh_out.write(item+"  ")
                fh_out.write("1"+'\n')
            fh_out.close()
            temp_fh.close()


def drawparams_maker(Ks,inds):
    for k in Ks:
        temp_name = "drawparams_K{}".format(k)
        fh_temp = open(temp_name, 'a')
        fh_temp.write('''
PARAMETERS FOR THE PROGRAM distruct.  YOU WILL NEED TO SET THESE
IN ORDER TO RUN THE PROGRAM.  

"(int)" means that this takes an integer value.
"(B)"   means that this variable is Boolean 
        (1 for True, and 0 for False)
"(str)" means that this is a string (but not enclosed in quotes) 
"(d)"   means that this is a double (a real number).

Data settings

#define INFILE_POPQ        K{0}.popq      // (str) input file of population q's
#define INFILE_INDIVQ      K{0}.indq    // (str) input file of individual q's
#define INFILE_LABEL_BELOW K{0}.names     // (str) input file of labels for below figure
#define INFILE_LABEL_ATOP  K{0}.languages // (str) input file of labels for atop figure
#define INFILE_CLUST_PERM  K{0}.perm     // (str) input file of permutation of clusters to print  
#define OUTFILE            K{0}.ps       //(str) name of output file

#define K	{0}    // (int) number of clusters	
#define NUMPOPS {1}    // (int) number of pre-defined populations
#define NUMINDS {1}  // (int) number of individuals

Main usage options

#define PRINT_INDIVS      0  // (B) 1 if indiv q's are to be printed, 0 if only population q's
#define PRINT_LABEL_ATOP  1  // (B) print labels above figure
#define PRINT_LABEL_BELOW 0  // (B) print labels below figure
#define PRINT_SEP         1  // (B) print lines to separate populations

Figure appearance

#define FONTHEIGHT 4	// (d) size of font
#define DIST_ABOVE 5	// (d) distance above plot to place text
#define DIST_BELOW -7	// (d) distance below plot to place text
#define BOXHEIGHT  100	// (d) height of the figure
#define INDIVWIDTH 8	// (d) width of an individual


Extra options

#define ORIENTATION 0	     // (int) 0 for horizontal orientation (default)
			     //       1 for vertical orientation
			     //	      2 for reverse horizontal orientation
                             //       3 for reverse vertical orientation
#define XORIGIN 100		// (d) lower-left x-coordinate of figure
#define YORIGIN 100		// (d) lower-left y-coordinate of figure
#define XSCALE 1		// (d) scale for x direction
#define YSCALE 1		// (d) scale for y direction
#define ANGLE_LABEL_ATOP 60	// (d) angle for labels atop figure (in [0,180])
#define ANGLE_LABEL_BELOW 60    // (d) angle for labels below figure (in [0,180])
#define LINEWIDTH_RIM  2	// (d) width of "pen" for rim of box
#define LINEWIDTH_SEP 0.4	// (d) width of "pen" for separators between pops and for tics
#define LINEWIDTH_IND 0.4	// (d) width of "pen" used for individuals 
#define GRAYSCALE 0	        // (B) use grayscale instead of colors
#define ECHO_DATA 1             // (B) print some of the data to the screen
#define REPRINT_DATA 1          // (B) print the data as a comment in the ps file
#define PRINT_INFILE_NAME 0     // (B) print the name of INFILE_POPQ above the figure 
                                //     this option is meant for use only with ORIENTATION=0 
#define PRINT_COLOR_BREWER 1    // (B) print ColorBrewer settings in the output file 
                                //     this option adds 1689 lines and 104656 bytes to the output
                                //     and is required if using ColorBrewer colors

'''.format(k,inds))
        fh_temp.close()

def distruction(Ks):
    for k in Ks:
        distruct_call = "./distruct -d drawparams_K{0} -p K{0}.popq".format(k)
        proc_distruct = sp.call(distruct_call, shell=True)


popq_maker()
drawparams_maker(k_list,inds)
distruction(k_list)
