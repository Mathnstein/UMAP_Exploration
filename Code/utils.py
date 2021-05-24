import numpy as np
from random import sample
from sklearn.neighbors import NearestNeighbors
from scipy.stats import beta

def scale(X: np.array):
    return (X-np.mean(X,axis=0))/np.std(X,axis=0)

def hopkins(X: np.array, alpha=0.05):
    '''
    Hopkins is a metric of how uniformly distributed an array is.
        - Close to 1 is evidence of substructure
        - Close to .5 is normally distributed
        - Close to 0 indicates regularity
    Input: 
        X: An (n,) or (n,m) list or numpy array
    
    Output:
        H: float, Hopkin's Statistic
        D: string, Decision on if we have regularity, no structure, or clusters
        p: float, P-Value from the cdf of Beta(m,m) distribution
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
        ujd.append(u_dist[0][1]**d)
        # Get distance to another sample
        random_sample = X[rand_X[j]].reshape(1,-1)
        w_dist, _ = nbrs.kneighbors(random_sample, 2, return_distance=True)
        wjd.append(w_dist[0][1]**d)
    denom = np.sum(ujd) + np.sum(wjd)
    if denom == 0:
        raise RuntimeWarning('The Hopkins denominator was 0, cannot proceed')
    else:
        H = np.sum(ujd) / denom
        if H > 0.5:
            p = 1 - beta.cdf(H, m, m)
            if p < alpha:
                D = 'There is evidence of clusters'
            else:
                D = 'There is no evidence of structure'
        else:
            p = beta.cdf(H, m, m)
            if p < alpha:
                D = 'There is evidence of regularity'
            else:
                D = 'There is no evidence of structure'
    return H, D, p

def average_hopkins(X: np.array, labels: np.array, alpha=0.05):
    H = 0
    unique_labels = np.unique(labels)
    c = len(unique_labels)
    bRejectedAll = True
    for ul in unique_labels:
        bKeep = labels == ul
        # We scale down by how many clusters we test for to get a family alpha
        h, _, p = hopkins(X[bKeep, :], alpha/c)
        H += h/c
        bRejectedAll &= p < alpha/c
        print(ul, h, p)
    return H, bRejectedAll

