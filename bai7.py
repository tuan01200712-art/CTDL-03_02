INF = float('inf')

adj = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 5)],
    4: [(5, 2)],
    5: []
}

def dijkstra_path(adj, s, t):
    n = len(adj)

    dist = [INF] * n
    visited = [False] * n
    parent = [-1] * n

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

            if not visited[v] and dist[u] + w < dist[v]:

                dist[v] = dist[u] + w

                # Lưu đỉnh cha
                parent[v] = u

    # Truy vết đường đi
    path = []

    current = t

    while current != -1:
        path.append(current)
        current = parent[current]

    path.reverse()

    return dist[t], path

distance, path = dijkstra_path(adj, 0, 4)

print("Độ dài:", distance)
print("Đường đi:", " -> ".join(map(str, path)))