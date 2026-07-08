import heapq

adj = {
    0: [(1,1), (2,2)],
    1: [(3,3)],
    2: [(3,2)],
    3: [(4,1)],
    4: []
}

def k_shortest_paths(adj, s, t, K):

    n = len(adj)

    count = [0] * n

    heap = [(0, s)]

    answers = []

    while heap:

        dist, u = heapq.heappop(heap)

        count[u] += 1

        if count[u] > K:
            continue

        if u == t:

            answers.append(dist)

            if len(answers) == K:
                return answers

        for v, w in adj[u]:

            heapq.heappush(
                heap,
                (dist + w, v)
            )

    return answers


print(
    k_shortest_paths(
        adj,
        0,
        4,
        3
    )
)