# Phylo_Wrapper_Scripts

This directory contains several scripts designed to automate working with several commonly used phylogenetics or phylogeography programs:

1) Admixture: An alternative to STRUCTURE to investigate population structuring. Allows user to select number of K's to test and number of replicates per K. Summarizes outputs of each log file to allow plotting of cross-validation error for each K value. Designed to work with a directory containing multiple input files. Also contains R scripts for plotting cross-validation error and for making barplots for K values.

2) clumpp & distruct: Workflow to create graphical representations of STRUCTURE outputs. Helps automate usage of each program for typical output of something like STRUCTURE Harvester.

3) RAxML: Automate running raxml across any number of phylip alignment files in a given directory. Easy to edit call of raxml within the script to achieve various outcomes.

There is also a more general use script that serves to rename taxa or samples across any type of text file (ie all input files for phylo programs). This works for a single input file or can be used to change names across any number of input files present in a single directory.


**Contact:**

Daniel Portik, PhD

Postdoctoral Researcher

University of Arizona

daniel.portik@gmail.com

