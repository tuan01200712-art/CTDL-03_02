import heapq

def dijkstra_heap(adj, source):

    INF = float('inf')
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

                heapq.heappush(
                    heap,
                    (new_dist, v)
                )

    return dist