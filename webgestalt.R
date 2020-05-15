webgestalt <- function(topic){
library(devtools)
install_github("bzhanglab/WebGestaltR")
install_bitbucket("ibi_group/disgenet2r")

install.packages("WebGestaltR")

library("WebGestaltR")
library("disgenet2r")
library(httr)
library(jsonlite)
library(lubridate)
options(stringsAsFactors = FALSE)


library("readxl")
diseaseIDtab <- read_excel("C:\\TNO\\2019\\20191003_Exposome\\disease_mappings_converted.xlsx", sheet = 1, col_names = TRUE, col_types = "text")

## Arguments
args = commandArgs(trailingOnly=TRUE)
topic <- args[1]

## Gene list
#topic <- "asthma"
geneList0 <- (((read.csv(paste("C:\\TNO\\2019\\20191003_Exposome\\output\\",topic,"_protein_list.txt", sep = ""), header = FALSE, stringsAsFactors = FALSE))))

geneList2 <- as.data.frame(geneList0)

## Output directory WebGestalt if "isOutput" = TRUE
outputdir <- paste("C:\\TNO\\2019\\20191003_Exposome\\output\\webgestalt\\","outputWebGestaltR\\", sep = "")

## WebGestalt
outputWebGestalt <- WebGestaltR(enrichMethod = "ORA", organism = "hsapiens",
                                enrichDatabase = "disease_Disgenet", enrichDatabaseFile = NULL,
                                enrichDatabaseType = "genesymbol", enrichDatabaseDescriptionFile = NULL,
                                interestGeneFile = NULL, interestGene = geneList2[,1],
                                interestGeneType = "genesymbol", collapseMethod = "mean",
                                referenceGeneFile = NULL, referenceGene = NULL,
                                referenceGeneType = NULL, referenceSet = "genome", minNum = 5,
                                maxNum = 2000, sigMethod = "fdr", fdrMethod = "BH", fdrThr = 0.05,
                                topThr = 100, reportNum = 20, perNum = 1000, isOutput = TRUE,
                                outputDirectory = outputdir, projectName = NULL,
                                dagColor = "continuous", setCoverNum = 10,
                                networkConstructionMethod = NULL, neighborNum = 10,
                                highlightType = "Seeds", highlightSeedNum = 10, nThreads = 1,
                                hostName = "http://www.webgestalt.org/")

diseaseIDtab <- diseaseIDtab[which(diseaseIDtab$vocabulary=="MSH" | diseaseIDtab$vocabulary=="DO" | diseaseIDtab$vocabulary=="HPO"),]

colnames(outputWebGestalt)[1] <- "diseaseId"

outputWebGestalt2 <- merge(x = outputWebGestalt, y = diseaseIDtab, by = "diseaseId", all.x = TRUE)

write.table(outputWebGestalt2, file = paste("C:\\TNO\\2019\\20191003_Exposome\\output\\webgestalt\\Gene_Disease_relation_MESH_DO_HPO3_",topic,".csv", sep = ""), sep = "\t", row.names = FALSE, col.names = TRUE,quote=TRUE)
}