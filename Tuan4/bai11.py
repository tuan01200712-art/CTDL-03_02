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

def multi_source_dijkstra(adj, sources):

    n = len(adj)

    dist = [INF] * n

    heap = []

    # Khởi tạo nhiều nguồn
    for s in sources:
        dist[s] = 0
        heapq.heappush(heap, (0, s))

    while heap:

        current_dist, u = heapq.heappop(heap)

        if current_dist > dist[u]:
            continue

        for v, w in adj[u]:

            new_dist = dist[u] + w

            if new_dist < dist[v]:

                dist[v] = new_dist

                heapq.heappush(
                    heap,
                    (new_dist, v)
                )

    return dist


sources = [0, 3]

result = multi_source_dijkstra(adj, sources)

print("Khoảng cách tới nguồn gần nhất:")
print(result)