#Create simple barplots from Q files resulting from admixture, colors are randomly assigned
#from the rainbow pallette 

#####################################

#Clade1

####################################

tbl2=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade1_fixed_Outputs/Clade1_fixed.2.Q.rep1")
barplot(t(as.matrix(tbl2)), col=rainbow(2), xlab="Individual #", ylab="Ancestry", space=0, names.arg = row.names(tbl2), cex.names = 0.3)

tbl3=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade1_fixed_Outputs/Clade1_fixed.3.Q.rep1")
barplot(t(as.matrix(tbl3)), col=rainbow(3), xlab="Individual #", ylab="Ancestry", space=0)

tbl4=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade1_fixed_Outputs/Clade1_fixed.4.Q.rep1")
barplot(t(as.matrix(tbl4)), col=rainbow(4), xlab="Individual #", ylab="Ancestry", space=0)

tbl5=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade1_fixed_Outputs/Clade1_fixed.5.Q.rep1")
barplot(t(as.matrix(tbl5)), col=rainbow(5), xlab="Individual #", ylab="Ancestry", space=0)

tbl6=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade1_fixed_Outputs/Clade1_fixed.6.Q.rep1")
barplot(t(as.matrix(tbl6)), col=rainbow(6), xlab="Individual #", ylab="Ancestry", space=0)

tbl7=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade1_fixed_Outputs/Clade1_fixed.7.Q.rep1")
barplot(t(as.matrix(tbl7)), col=rainbow(7), xlab="Individual #", ylab="Ancestry", space=0)

tbl8=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade1_fixed_Outputs/Clade1_fixed.8.Q.rep1")
barplot(t(as.matrix(tbl8)), col=rainbow(8), xlab="Individual #", ylab="Ancestry", space=0)

tbl9=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade1_fixed_Outputs/Clade1_fixed.9.Q.rep1")
barplot(t(as.matrix(tbl9)), col=rainbow(9), xlab="Individual #", ylab="Ancestry", space=0)

tbl10=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade1_fixed_Outputs/Clade1_fixed.10.Q.rep1")
barplot(t(as.matrix(tbl10)), col=rainbow(10), xlab="Individual #", ylab="Ancestry", space=0)



#####################################

#Clade2

####################################

tbl2=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade2_fixed_Outputs/Clade2_fixed.2.Q.rep1")
barplot(t(as.matrix(tbl2)), col=rainbow(2), xlab="Individual #", ylab="Ancestry", space=0)

tbl3=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade2_fixed_Outputs/Clade2_fixed.3.Q.rep1")
barplot(t(as.matrix(tbl3)), col=rainbow(3), xlab="Individual #", ylab="Ancestry", space=0)

tbl4=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade2_fixed_Outputs/Clade2_fixed.4.Q.rep1")
barplot(t(as.matrix(tbl4)), col=rainbow(4), xlab="Individual #", ylab="Ancestry", space=0)

tbl5=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade2_fixed_Outputs/Clade2_fixed.5.Q.rep1")
barplot(t(as.matrix(tbl5)), col=rainbow(5), xlab="Individual #", ylab="Ancestry", space=0)

tbl6=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade2_fixed_Outputs/Clade2_fixed.6.Q.rep1")
barplot(t(as.matrix(tbl6)), col=rainbow(6), xlab="Individual #", ylab="Ancestry", space=0)

tbl7=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade2_fixed_Outputs/Clade2_fixed.7.Q.rep1")
barplot(t(as.matrix(tbl7)), col=rainbow(7), xlab="Individual #", ylab="Ancestry", space=0)

tbl8=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade2_fixed_Outputs/Clade2_fixed.8.Q.rep1")
barplot(t(as.matrix(tbl8)), col=rainbow(8), xlab="Individual #", ylab="Ancestry", space=0)

tbl9=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade2_fixed_Outputs/Clade2_fixed.9.Q.rep1")
barplot(t(as.matrix(tbl9)), col=rainbow(9), xlab="Individual #", ylab="Ancestry", space=0)


#####################################

#Clade3

####################################

tbl2=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade3_fixed_Outputs/Clade3_fixed.2.Q.rep1")
barplot(t(as.matrix(tbl2)), col=rainbow(2), xlab="Individual #", ylab="Ancestry", space=0)

tbl3=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade3_fixed_Outputs/Clade3_fixed.3.Q.rep1")
barplot(t(as.matrix(tbl3)), col=rainbow(3), xlab="Individual #", ylab="Ancestry", space=0)

tbl4=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade3_fixed_Outputs/Clade3_fixed.4.Q.rep1")
barplot(t(as.matrix(tbl4)), col=rainbow(4), xlab="Individual #", ylab="Ancestry", space=0)

tbl5=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade3_fixed_Outputs/Clade3_fixed.5.Q.rep1")
barplot(t(as.matrix(tbl5)), col=rainbow(5), xlab="Individual #", ylab="Ancestry", space=0)

tbl6=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade3_fixed_Outputs/Clade3_fixed.6.Q.rep1")
barplot(t(as.matrix(tbl6)), col=rainbow(6), xlab="Individual #", ylab="Ancestry", space=0)

tbl7=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade3_fixed_Outputs/Clade3_fixed.7.Q.rep1")
barplot(t(as.matrix(tbl7)), col=rainbow(7), xlab="Individual #", ylab="Ancestry", space=0)

tbl8=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade3_fixed_Outputs/Clade3_fixed.8.Q.rep1")
barplot(t(as.matrix(tbl8)), col=rainbow(8), xlab="Individual #", ylab="Ancestry", space=0)

tbl9=read.table("/Volumes/West_Africa/West_Africa/Conraua_Final/6_Newer_Analyses/Admixture/Clade3_fixed_Outputs/Clade3_fixed.9.Q.rep1")
barplot(t(as.matrix(tbl9)), col=rainbow(9), xlab="Individual #", ylab="Ancestry", space=0)

