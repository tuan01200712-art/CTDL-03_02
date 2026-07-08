import heapq

INF = float('inf')

adj = {
    0: [(1,4), (2,2)],
    1: [(3,5)],
    2: [(3,8)],
    3: []
}

def minimax_path(adj, source):

    n = len(adj)

    dist = [INF] * n

    dist[source] = 0

    heap = [(0, source)]

    while heap:

        bottleneck, u = heapq.heappop(heap)

        if bottleneck > dist[u]:
            continue

        for v, w in adj[u]:

            new_dist = max(
                dist[u],
                w
            )

            if new_dist < dist[v]:

                dist[v] = new_dist

                heapq.heappush(
                    heap,
                    (new_dist, v)
                )

    return dist


result = minimax_path(adj, 0)

print(result)