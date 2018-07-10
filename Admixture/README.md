# admixture_wrapper_complete.py

admixture_wrapper_complete.py [directory with ped and map files ("recoded 12" ped files)]

Will run program admixture on a directory of ped files, each assumed to have
a unique prefix. User selects range of K values and number of replicates
per K. The Q, P, and log files are written to a directory with the same
name as the prefix of each ped file. After completing analyses for a
ped file, the log files will be summarized to obtain the cross-validation
error values for each replicate per K, and an average and SD will be
calculated which can be easily plotted with the associated R script.
I also include an example R script to create stacked barplots.

You may need to recode your ped files with the plink program to get 
Admixture to run properly. I use plink --recode12 for my ped files.


Written for Python 2.7

External Dependencies: Admixture (in path), numpy

 
**Contact:**

Daniel Portik, PhD

Postdoctoral Researcher

University of Arizona

daniel.portik@gmail.com
