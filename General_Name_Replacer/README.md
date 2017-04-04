# General_Name_Replacer.py

This script uses a tab-delimited text file to replace string matches with a new string. I use it to replace taxon or sample names in the input files I use for phylogenetics and phylogeography programs. The search will replace the biggest names first, so if a starting name is contained within another starting name (ex. Pop1_sample1, Pop1_sample10) this is not a problem.

The original version works with a single file, the bin version will replace names within all the files occurring in the target directory.
