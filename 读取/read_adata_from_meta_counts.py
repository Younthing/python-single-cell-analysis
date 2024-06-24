# %%
import pandas as pd
import scipy.sparse
from pathlib import Path

meta_data = pd.read_table("GSE134003_ClusterMetadata.txt.gz", index_col=0)
# %%

counts = pd.read_table("./GSE134003_SI_SNI_rawcounts.txt.gz", index_col=0)
# %%
import scanpy as sc

adata = sc.AnnData(counts.T, obs=meta_data)
adata.obs["group"] = adata.obs["Condition"]
adata.obs["batch"] = adata.obs["Sample"]

adata.obs = adata.obs.drop(adata.obs.columns[:6], axis=1)

# 确保变量名唯一
adata.var_names_make_unique()
# %%

# 确保是保存的是浮点数
adata.X = adata.X.astype(float)
# 确保表达矩阵是稀疏格式
if not scipy.sparse.issparse(adata.X):
    adata.X = scipy.sparse.csr_matrix(adata.X)


output_file = Path("anndata_raw.h5ad")
adata.write_h5ad(output_file)
