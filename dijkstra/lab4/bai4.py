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

dist = [INF] * n
visited = [False] * n

dist[s] = 0

# Dijkstra O(V²)
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

# In kết quả
print("Khoảng cách từ đỉnh", s)

for i in range(n):
    if dist[i] == INF:
        print(f"dist[{i}] = -1")
    else:
        print(f"dist[{i}] = {dist[i]}")