no_cities = 5
roads = [
    (0, 1, 0.4),
    (0, 2, 1.2),
    (1, 3, 0.1),
    (1, 4, 0.6),
    (2, 3, 0.5),
    (3, 4, 0.1)
]

from math import inf
dist = [
    # 0,   1,   2,   3,   4
    [ 0, inf, inf, inf, inf ], # city 0
    [inf,  0, inf, inf, inf ], # city 1
    [inf, inf,  0, inf, inf ], # city 2
    [inf, inf, inf,  0, inf ], # city 3
    [inf, inf, inf, inf,  0 ]  # city 4
]
for i,j,d in roads:
    dist[i][j] = dist[j][i] = d

for k in range(no_cities):
    for i in range(no_cities):
        for j in range(no_cities):
            dist[i][j] = dist[j][i] = \
                min(dist[i][j], dist[i][k] + dist[k][j])

print(dist)
