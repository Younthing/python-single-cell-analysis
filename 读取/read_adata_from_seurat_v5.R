library(Seurat)

sce <- readRDS("./rep2/sc_data_anno.rds")

sce_new <- as.SingleCellExperiment(sce, assay = c("RNA"))
library(zellkonverter)
writeH5AD(sce_new, "sce_obj.h5ad", X_name = "counts")
