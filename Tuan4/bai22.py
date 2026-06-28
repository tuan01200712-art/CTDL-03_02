import heapq

def shortest_with_k_edges(adj, s, t, k):

    INF = float('inf')

    n = len(adj)

    dist = [
        [INF] * (k + 2)
        for _ in range(n)
    ]

    dist[s][0] = 0

    heap = [(0, s, 0)]

    while heap:

        cost, u, used = heapq.heappop(heap)

        if u == t:
            return cost

        if cost > dist[u][used]:
            continue

        if used == k + 1:
            continue

        for v, w in adj[u]:

            new_cost = cost + w

            if new_cost < dist[v][used + 1]:

                dist[v][used + 1] = new_cost

                heapq.heappush(
                    heap,
                    (
                        new_cost,
                        v,
                        used + 1
                    )
                )

    return -1


adj = {
    0:[(1,100),(2,500)],
    1:[(2,100),(3,600)],
    2:[(3,100)],
    3:[]
}

print(
    shortest_with_k_edges(
        adj,
        0,
        3,
        2
    )
)