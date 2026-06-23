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

def second_shortest_path(adj, s, t):

    n = len(adj)

    first = [INF] * n
    second = [INF] * n

    first[s] = 0

    heap = [(0, s)]

    while heap:

        dist_u, u = heapq.heappop(heap)

        for v, w in adj[u]:

            new_dist = dist_u + w

            # tìm đường tốt nhất
            if new_dist < first[v]:

                second[v] = first[v]
                first[v] = new_dist

                heapq.heappush(heap, (first[v], v))

            # tìm đường tốt thứ hai
            elif first[v] < new_dist < second[v]:

                second[v] = new_dist

                heapq.heappush(heap, (second[v], v))

    return first[t], second[t]


shortest, second_shortest = second_shortest_path(adj, 0, 5)

print("Ngắn nhất:", shortest)
print("Ngắn nhì :", second_shortest)