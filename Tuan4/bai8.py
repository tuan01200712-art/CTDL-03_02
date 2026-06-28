INF = float('inf')

adj = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 5)],
    4: [(5, 2)],
    5: []
}

def dijkstra(adj, s):
    n = len(adj)

    dist = [INF] * n
    visited = [False] * n

    dist[s] = 0

    for _ in range(n):

        u = -1
        min_dist = INF

        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v, w in adj[u]:
            if not visited[v]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    return dist


s = 0
D = 3

dist = dijkstra(adj, s)

count = 0

for d in dist:
    if d <= D:
        count += 1

print("Khoảng cách:", dist)
print("Số đỉnh trong bán kính", D, "=", count)