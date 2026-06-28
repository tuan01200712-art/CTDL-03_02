import heapq

def dijkstra_state(adj, start, target, max_fuel):

    INF = float('inf')

    n = len(adj)

    dist = [
        [INF]*(max_fuel+1)
        for _ in range(n)
    ]

    dist[start][max_fuel] = 0

    heap = [(0, start, max_fuel)]

    while heap:

        cost, u, fuel = heapq.heappop(heap)

        if u == target:
            return cost

        if cost > dist[u][fuel]:
            continue

        for v, fuel_need in adj[u]:

            if fuel >= fuel_need:

                new_fuel = fuel - fuel_need

                new_cost = cost + fuel_need

                if new_cost < dist[v][new_fuel]:

                    dist[v][new_fuel] = new_cost

                    heapq.heappush(
                        heap,
                        (
                            new_cost,
                            v,
                            new_fuel
                        )
                    )

    return -1


adj = {
    0:[(1,2),(2,3)],
    1:[(3,2)],
    2:[(3,1)],
    3:[]
}

print(
    dijkstra_state(
        adj,
        0,
        3,
        5
    )
)