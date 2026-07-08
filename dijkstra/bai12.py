import heapq

INF = float('inf')

adj = {
    0: [(1,4), (2,1)],
    1: [(3,1)],
    2: [(1,2), (3,5), (4,8)],
    3: [(4,3), (5,5)],
    4: [(5,2)],
    5: []
}

def dijkstra(adj, source):

    n = len(adj)

    dist = [INF] * n
    dist[source] = 0

    heap = [(0, source)]

    while heap:

        current_dist, u = heapq.heappop(heap)

        if current_dist > dist[u]:
            continue

        for v, w in adj[u]:

            new_dist = dist[u] + w

            if new_dist < dist[v]:

                dist[v] = new_dist

                heapq.heappush(heap, (new_dist, v))

    return dist


s = 0
k = 2
t = 5

dist_from_s = dijkstra(adj, s)
dist_from_k = dijkstra(adj, k)

answer = dist_from_s[k] + dist_from_k[t]

print("Đường đi ngắn nhất qua đỉnh", k)
print("Chi phí =", answer)