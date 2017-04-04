rm(list=ls())
library(sfsmisc)

####################################
#Clade1
####################################
#Plots for Admixture cross-validation results
#****Change path below to correct file
Clade1 <- read.delim("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade1_fixed_Outputs/Clade1_fixed_cross_validation_averages.txt", header = TRUE, sep = "\t")
Clade1

ls(Clade1)
# Headers = "K" "CV_avg" "CV_sd" 


#Plot average cross-validation error against K value
plot(Clade1$K, Clade1$CV_avg, type = "b", pch=21, col="black", bg="gray", cex = 2, xlab = "K Value", ylab = "Cross-Validation Error")

#Use errbar function to Plot average cross-validation error (with SD error bars) against K value 
errbar(Clade1$K, Clade1$CV_avg, Clade1$CV_avg + Clade1$CV_sd, Clade1$CV_avg - Clade1$CV_sd, 
       pch=22, col="black", bg="gray", cex=2, xlab = "K Value", ylab = "Cross-Validation Error")



####################################
#Clade2
####################################
#Plots for Admixture cross-validation results
#****Change path below to correct file
Clade2 <- read.delim("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade2_fixed_Outputs/Clade2_fixed_cross_validation_averages.txt", header = TRUE, sep = "\t")
Clade2

ls(Clade2)
# Headers = "K" "CV_avg" "CV_sd" 


#Plot average cross-validation error against K value
plot(Clade2$K, Clade2$CV_avg, type = "b", pch=21, col="black", bg="gray", cex = 2, xlab = "K Value", ylab = "Cross-Validation Error")

#Use errbar function to Plot average cross-validation error (with SD error bars) against K value 
errbar(Clade2$K, Clade2$CV_avg, Clade2$CV_avg + Clade2$CV_sd, Clade2$CV_avg - Clade2$CV_sd, 
       pch=21, col="black", bg="gray", cex=2, xlab = "K Value", ylab = "Cross-Validation Error")


####################################
#Clade3
####################################
#Plots for Admixture cross-validation results
#****Change path below to correct file
Clade3 <- read.delim("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade3_fixed_Outputs/Clade3_fixed_cross_validation_averages.txt", header = TRUE, sep = "\t")
Clade3

ls(Clade3)
# Headers = "K" "CV_avg" "CV_sd" 


#Plot average cross-validation error against K value
plot(Clade3$K, Clade3$CV_avg, type = "b", pch=21, col="black", bg="gray", cex = 2, xlab = "K Value", ylab = "Cross-Validation Error")

#Use errbar function to Plot average cross-validation error (with SD error bars) against K value 
errbar(Clade3$K, Clade3$CV_avg, Clade3$CV_avg + Clade3$CV_sd, Clade3$CV_avg - Clade3$CV_sd, 
       pch=21, col="black", bg="gray", cex=2, xlab = "K Value", ylab = "Cross-Validation Error")


