# %%
import numpy as np
from numpy.lib.utils import source
import pandas as pd
import networkx as nx
import random

# %%
edges = pd.DataFrame()
edges['sources'] = list(range(10))
edges['targets'] = [random.randint(0, 9) for _ in range(10)]
edges['weights'] = [1] * 10
print(edges)

# %%
G = nx.from_pandas_edgelist(edges, source='sources', target='targets', edge_attr='weights')

# %%
nx.degree(G)
# %%
list(nx.connected_components(G))
# %%
nx.diameter(G)  # 图直径  最短的路径   非连通图没有
# %%
nx.degree_centrality(G)     # 度中心性

# %%
nx.eigenvector_centrality(G)  # 特征向量中心性
# %%
nx.betweenness_centrality(G)

# %%
nx.closeness_centrality(G)
# %%
nx.pagerank(G)

# %%
nx.hits(G)
# %%
