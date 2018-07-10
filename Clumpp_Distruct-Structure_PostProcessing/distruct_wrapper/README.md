# dictruction.py

Usage: python distruction.py [directory with all clumpp output files]

Reads K#.indq files in a directory. Makes a K#.popq file for each
to allow visualizing each individual as a separate, labeled bar.
Creates a drawparams file for each K for distruct, then creates
an output graphic for each K. You can add specific K#.perm files
to control which colors are used for which populations. You may also
need to edit this script to change the drawparams output, specifically
the BOXHEIGHT, INDIVWIDTH, ORIENTATION, XORIGIN, YORIGIN, and font
arguments to ensure your barplots will fit correctly. Edit it directly
in the script to use the same arguments for all the K's included.
Check the distruct manual for info on how these options work.


Written for Python 2.7

External Dependencies: distruct executable must be in same directory as clumpp output files


**Contact:**

Daniel Portik, PhD

Postdoctoral Researcher

University of Arizona

daniel.portik@gmail.com
