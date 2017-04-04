# raxml_wrapper.py

Usage: python raxml_wrapper.py [directory with all 'Contig.phylip' or 'Contig.phy' files]

example: 

`python dan/scripts/raxml_wrapper.py dan/exons/phylip_files`

Will run search directory for "NAME.phylip" files and the give option to execute raxml.
Moves best tree files with '.tre' extension added to output folder '/Best_trees'
Moves all other files from each run to '/Raxml_files'
Check these folders for progress.

Uses the following default command string to execute raxml:

`raxmlHPC -m GTRCAT -p 12345`

You can edit this in RAXML_string in the script. Change the settings you want,
but the input and output are automated so leave these strings out (-s, -n).
Add or change the analysis type here, using the syntax and flags of raxml.
If not running raxmlHPC, change program name below too.
KEEP the quotations around the string in the script or it will crash.


Examples of other useful command strings:

`raxmlHPC -m GTRCAT -p 12345` -----basic run for best tree

`raxmlHPC -m GTRCAT -p 12345 -# 20` -----for multiple (20) runs per file

`raxmlHPC -f a -m GTRCAT -p 12345 -x 12345 -# 100` ----for rapid bootstrapping (100 reps) and best ml tree

`raxmlHPC -x 12345 -p 12345 -# autoMRE -m GTRCAT` ----for  high auto stop rapid bootstrapping (up to 1000 reps) and best ml tree


I include a couple variations of the original script here so you can compare how to edit them.


Written for Python 2.7

External Dependencies: requires raxmlHPC to be in path (or another version like PTHREADS, in which case the string above needs to be changed)


# Dan Portik

daniel.portik@uta.edu

August 2015
