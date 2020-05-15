

topic <- "3A_Newborn"
geneList1 <- (((read.csv(paste("/Users/vanstee/Documents/TNO/SRP/INDRA/indra_output/Genes_3A_3B/",topic,"_protein_list.txt", sep = ""), header = FALSE, stringsAsFactors = FALSE))))

geneList <- geneList1[,1]

library("topGO")
library(reshape2)
library(GO.db)

## GO to Symbol mappings (only the BP ontology is used)
gene2GOid <- annFUN.org("BP", feasibleGenes = geneList, mapping = "org.Hs.eg.db", ID = "symbol")

# Set in dataframe object
gene2geneset <- melt(gene2GOid)
colnames(gene2geneset) <- c("gene", "genesetID")

# extract a named vector of all terms
gene2geneset$genesetTerm <- Term(gene2geneset$genesetID)

#write.table(gene2geneset, file = paste("/Users/vanstee/Documents/TNO/SRP/INDRA/indra_output/3B/Gene2GOterm_",topic,".csv", sep = ""), sep = "\t", row.names = FALSE, col.names = TRUE,quote=FALSE)



library(GSEABase)
myCollection <- GOCollection(gene2geneset$genesetID)

fl <- "http://www.geneontology.org/ontology/subsets/goslim_generic.obo"
slim <- getOBOCollection(fl)

test1 <- slim@.kv
test1 <- test1[test1$key=='is_a',]
colnames(test1)[1] <- "GOslimID"
?goSlim

testBP <- goSlim(myCollection, slim, "BP")
testMF <- goSlim(myCollection, slim, "MF")
testCC <- goSlim(myCollection, slim, "CC")

test <- goSlim(myCollection, slim, "BP", evidenceCode="ALL")


testBP$GOslimID <- rownames(testBP)

testMF$GOslimID <- rownames(testMF)

testCC$GOslimID <- rownames(testCC)

test0 <- rbind(testBP, testMF, testCC)

test02 <- merge(x = test0, y = test1, by = "GOslimID", all.x = TRUE)
colnames(test02)[6] <- "genesetID"

test3 <- merge(x = gene2geneset, y = test02, by = "genesetID", all.x = TRUE)

test3$key <- NULL


write.table(test3, file = paste("/Users/vanstee/Documents/TNO/SRP/INDRA/indra_output/3B/Gene2GOandGOslim1_",topic,".csv", sep = ""), sep = "\t", row.names = FALSE, col.names = TRUE,quote=FALSE)

test4 <- test3[which(!is.na(test3$GOslimID)),]

test5 <- unique(test4[,c(2,4:7)])

write.table(test5, file = paste("/Users/vanstee/Documents/TNO/SRP/INDRA/indra_output/3B/Gene2GOslim_",topic,".csv", sep = ""), sep = "\t", row.names = FALSE, col.names = TRUE,quote=FALSE)
