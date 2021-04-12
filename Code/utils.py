import numpy as np
from random import sample
from sklearn.neighbors import NearestNeighbors

def hopkins(X: np.array):
    '''
    Input: 
        X: n x m numpy array of floats
    
    Output:
        H: float, Hopkin's Statistic
    '''
    d = X.shape[1]
    n = len(X)
    m = int(0.1 * n)
    nbrs = NearestNeighbors(n_neighbors=1).fit(X)
    rand_X = sample(range(0, n, 1), m)
    ujd = []
    wjd = []
    for j in range(0, m):
        random_uniform = np.random.uniform(np.min(X, axis=0), np.max(X, axis=0), d).reshape(1,-1)
        u_dist, _ = nbrs.kneighbors(random_uniform, 2, return_distance=True)
        ujd.append(u_dist[0][1])
        random_sample = X[rand_X[j]].reshape(1,-1)
        w_dist, _ = nbrs.kneighbors(random_sample, 2, return_distance=True)
        wjd.append(w_dist[0][1])
    H = np.sum(ujd) / (np.sum(ujd) + np.sum(wjd))
    return H
