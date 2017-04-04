# Phylo_Wrapper_Scripts

This directory contains several scripts designed to automate working with several commonly used phylogenetics/phylogeography programs:

1) Admixture: An alternative to STRUCTURE to investigate population structuring. Allows user to select number of K's to test and number of replicates per K. Summarizes outputs of each log file to allow plotting of cross-validation error for each K value. Designed to work with a directory containing multiple input files.

2) clumpp & distruct: Workflow to create graphical representations of STRUCTURE outputs. Helps automate usage of each program for typical output of something like STRUCTURE Harvester.

3) RAxML: Automate running raxml across any number of phylip alignment files in a given directory. Easy to edit call of raxml within the script to achieve various outcomes.
