import heapq

adj = {
    0: [(1, 0.5), (2, 0.8)],
    1: [(3, 0.9)],
    2: [(3, 0.6)],
    3: []
}

def max_probability(adj, source):

    n = len(adj)

    prob = [0.0] * n
    prob[source] = 1.0

    heap = [(-1.0, source)]

    while heap:

        current_prob, u = heapq.heappop(heap)

        current_prob = -current_prob

        if current_prob < prob[u]:
            continue

        for v, p in adj[u]:

            new_prob = prob[u] * p

            if new_prob > prob[v]:

                prob[v] = new_prob

                heapq.heappush(
                    heap,
                    (-new_prob, v)
                )

    return prob

result = max_probability(adj, 0)

print(result)