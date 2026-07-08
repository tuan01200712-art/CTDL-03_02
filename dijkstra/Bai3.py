INF = float('inf')

# Đồ thị G1
adj = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 5)],
    4: [(5, 2)],
    5: []
}

n = 6
s = 0

# Khởi tạo
dist = [INF] * n
visited = [False] * n

dist[s] = 0

# Dijkstra O(V²)
for _ in range(n):

    u = -1
    min_dist = INF

    # Tìm đỉnh chưa xét có dist nhỏ nhất
    for i in range(n):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i

    if u == -1:
        break

    visited[u] = True

    # Relax các cạnh kề
    for v, w in adj[u]:
        if not visited[v]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

print("Khoảng cách ngắn nhất từ đỉnh", s)
print(dist)