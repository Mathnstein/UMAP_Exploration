import numpy as np
from random import sample
from sklearn.neighbors import NearestNeighbors

def hopkins(X: np.array):
    '''
    Hopkins is a metric of how uniformly distributed an array is.
        - Close to 1 is evidence of substructure
        - Close to .5 is normally distributed
        - Close to 0 indicates regularity
    Input: 
        X: An (n,) or (n,m) list or numpy array
    
    Output:
        H: float, Hopkin's Statistic
    '''
    X = np.array(X)
    if len(X.shape) == 1:
        X = X.reshape(-1,1)
    d = X.shape[1]
    n = len(X)
    m = int(0.1 * n)
    nbrs = NearestNeighbors(n_neighbors=1).fit(X)
    rand_X = sample(range(0, n, 1), m)
    ujd = []
    wjd = []
    for j in range(0, m):
        # Get distance to a random point
        random_uniform = np.random.uniform(np.min(X, axis=0), np.max(X, axis=0), d).reshape(1,-1)
        u_dist, _ = nbrs.kneighbors(random_uniform, 2, return_distance=True)
        ujd.append(u_dist[0][1])
        # Get distance to another sample
        random_sample = X[rand_X[j]].reshape(1,-1)
        w_dist, _ = nbrs.kneighbors(random_sample, 2, return_distance=True)
        wjd.append(w_dist[0][1])
    denom = np.sum(ujd) + np.sum(wjd)
    if denom == 0:
        raise RuntimeWarning('The Hopkins denominator was 0, cannot proceed')
    else:
        H = np.sum(ujd) / denom
    return H

