INF = float('inf')

adj = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 5)],
    4: [(5, 2)],
    5: []
}

def dijkstra_shortest(adj, s, t):
    n = len(adj)

    dist = [INF] * n
    visited = [False] * n

    dist[s] = 0

    for _ in range(n):

        u = -1
        min_dist = INF

        # Tìm đỉnh gần nhất
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:
            break

        # Nếu đã tới đích thì dừng
        if u == t:
            return dist[t]

        visited[u] = True

        # Relax cạnh
        for v, w in adj[u]:
            if not visited[v]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    return dist[t]

s = 0
t = 4

print("Khoảng cách ngắn nhất:", dijkstra_shortest(adj, s, t))