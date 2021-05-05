import numpy as np


x = [2, 5, 3, 7, 5]
N = len(x)

CS = np.zeros(N+1)
CS[1:] = np.cumsum(x)
def S(i,j):
    return CS[j] - CS[i]

def P(N, K):
    PT = np.zeros((N+1,K+1), dtype = int)
	# Base cases
    for i in range(N+1):
        PT[i,1] = S(0,i)
    for j in range(2,K+1):
        PT[0,j] = 0

	# Recursive case
    for i in range(1,N+1):
        for j in range(2,K+1):
            PT[i,j] = min(max(PT[m,j-1], S(m,i)) 
                          for m in range(i))
    return PT[N, K]

for k in range(1,N):
    print(k, 'paritionings:', P(N, k))

