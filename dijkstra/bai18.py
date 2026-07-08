INF = float('inf')

n = 3

edges = [
    (0, 1, 2),
    (0, 2, 5),
    (2, 1, -4)
]

dist = [INF] * n
dist[0] = 0

for _ in range(n - 1):

    for u, v, w in edges:

        if dist[u] != INF and dist[u] + w < dist[v]:

            dist[v] = dist[u] + w

print(dist)