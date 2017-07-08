# General_Name_Replacer.py

This script uses a tab-delimited text file to replace string matches with a new string (see example file). Please note each line should end with a newline break (\n), and NOT a carriage return (\r). Please make sure your file is in this correct format or you will likely experience problems.


I use these scripts to replace taxon or sample names in the input files I use for phylogenetics and phylogeography programs. The search will replace the biggest names first, so if a starting name is contained within another starting name (ex. Pop1_sample1, Pop1_sample10) this is not a problem. That is, if some names are substrings of other strings, the order in which they are replaced will ensure the replacement name is the correct match. This was particularly helpful when renaming sequencing sample names to museum codes or taxon name across large sets of files generated from sequence capture data.


The original version works with a single file, the bin version will replace names within all the files occurring in the target directory.
