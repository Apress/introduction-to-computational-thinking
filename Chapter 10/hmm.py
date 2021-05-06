import numpy as np

def forward(X, pi, T, E):
    N = len(X)
    K = T.shape[0]
    F = np.zeros((K,N))
    F[:,0] = pi * E[:,X[0]]
    for i in range(1, N):
        for k in range(K):
            F[k, i] = E[k, X[i]] * sum(T[:, k] * F[:, i-1])
    return F

def likelihood(X, pi, T, E):
    F = forward(X, pi, T, E)
    return sum(F[:,len(X) - 1])

X = (0, 0, 1, 0)
pi = [0.5,0.4]
T = np.array((
    [0.1, 0.9],
    [0.2, 0.8]
))
E = np.array([
    [0.4, 0.4, 0.2],
    [0.2, 0.2, 0.6]
])

print(forward(X, pi, T, E))
print(likelihood(X, pi, T, E))


def scale_forward(X, pi, T, E):
    N = len(X)
    K = T.shape[0]
    F = np.zeros((K,N))
    scales = np.zeros(N)

    F[:,0] = pi * E[:,X[0]]
    scales[0] = sum(F[:,0])
    F[:,0] /= scales[0]

    for i in range(1, N):
        for k in range(K):
            F[k, i] = E[k, X[i]] * sum(T[:, k] * F[:, i-1])
        scales[i] = sum(F[:,i])
        F[:,i] /= scales[i]

    return F, scales

def scale_log_likelihood(X, pi, T, E):
    _, scales = scale_forward(X, pi, T, E)
    return sum(np.log(scales))

print(scale_forward(X, pi, T, E))
print(scale_log_likelihood(X, pi, T, E))
print(np.log(likelihood(X, pi, T, E)))

