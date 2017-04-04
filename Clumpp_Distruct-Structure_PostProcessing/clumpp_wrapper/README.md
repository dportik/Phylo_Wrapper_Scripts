# clumpp_wrapper_ind.py

Usage: python clumpp_wrapper.py [directory with all clumpp indfiles]

Executes CLUMPP across a bin of 'K#.indfile' files, ideally resulting from
something like Structure Harvester.  Requires user input of number of individuals
and number of replicates per K, then executes across all indfiles automating
some necessary information.

The paramfile should also be in this directory. NOTE that not all commands in the
paramfile will be overwritten with command line arguments.  See bottom for commands 
able to be included, and check all remaining params in the file to ensure they 
are in fact correct.  

If this doesn't work right the first time, delete all generated outputs or it 
will simply continue adding to those files and create problems for the next step.


Written for Python 2.7

External Dependencies: clumpp executable must be in same directory as clumpp indfiles


# Dan Portik

daniel.portik@uta.edu

March 2016
