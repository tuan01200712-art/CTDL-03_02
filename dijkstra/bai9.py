import heapq

INF = float('inf')

adj = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 5)],
    4: [(5, 2)],
    5: []
}

def dijkstra_heap(adj, source):
    n = len(adj)

    dist = [INF] * n
    dist[source] = 0

    pq = []
    heapq.heappush(pq, (0, source))

    while pq:

        current_dist, u = heapq.heappop(pq)

        # Bỏ qua bản ghi cũ
        if current_dist > dist[u]:
            continue

        for v, w in adj[u]:

            new_dist = dist[u] + w

            if new_dist < dist[v]:

                dist[v] = new_dist

                heapq.heappush(
                    pq,
                    (new_dist, v)
                )

    return dist

result = dijkstra_heap(adj, 0)

print("Khoảng cách ngắn nhất:")
print(result)