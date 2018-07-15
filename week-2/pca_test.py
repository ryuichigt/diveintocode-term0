import numpy as np
from sklearn.decomposition import PCA

np.random.seed(0)
X = np.random.randint(10, size = (3,3))


# 共分散行列を求める
X_bar = np.array([row - np.mean(row) for row in X.transpose()]).transpose()
m = np.dot(X_bar.T, X_bar) / X.shape[0]

# 固有値問題を解く
(w, v) = np.linalg.eig(m)
v = v.T
print(v)
# 固有値の大きい順に固有値と固有ベクトルをソート
tmp = {}
for i, value in enumerate(w):
	tmp[value] = i

v_sorted = []
for key in sorted(tmp.keys(), reverse=True):
	v_sorted.append(v[tmp[key]])
v_sorted = np.array(v_sorted)
w_sorted = np.array(sorted(w, reverse=True))

# 次元削減
dim = 2
components = v_sorted[:dim,]


X_pca = np.dot(X_bar, components.T)

# 主成分分析後のサイズ
X_pca.shape

pca = PCA()

pca = pca.fit_transform(X)

