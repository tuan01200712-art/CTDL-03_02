INF = float('inf')

adj = {
    0: [(1,4), (2,1)],
    1: [(3,1)],
    2: [(1,2), (3,5), (4,8)],
    3: [(4,3), (5,5)],
    4: [(5,2)],
    5: []
}

n = 6
source = 0

dist = [INF] * n
visited = [False] * n

dist[source] = 0

print("Ban dau:")
print(dist)

for step in range(n):

    # Chọn đỉnh chưa xét có khoảng cách nhỏ nhất
    u = -1
    min_dist = INF

    for i in range(n):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i

    if u == -1:
        break

    visited[u] = True

    print(f"\nBuoc {step + 1}: Chot dinh {u}")

    # Relax các cạnh
    for v, w in adj[u]:
        if not visited[v] and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

    print("dist =", dist)

print("\nKet qua cuoi cung:")
print(dist)