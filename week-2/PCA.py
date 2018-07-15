import numpy as np
import numpy.random as random

random.seed(0)
X = np.random.randint(10, size = (6,6))

#主成分分析関数
def PCA(P):
    m = sum(P) / float(len(P))
    P_m = P - m
    l,v = np.linalg.eig(np.dot(P_m.T,P_m) )
    return v.T

pca = PCA(X)
print (pca)

