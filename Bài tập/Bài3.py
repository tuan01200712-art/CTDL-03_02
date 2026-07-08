def bellmanFord(vertices, edges, source):
    dist = [float("inf")] * vertices
    dist[source] = 0

    for i in range(vertices - 1):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            print("Đồ thị có chu trình âm")
            return

    print("Khoảng cách ngắn nhất:")
    for i in range(vertices):
        print("Đỉnh", i, "=", dist[i])


edges = [
    (0, 1, 2),
    (0, 2, 5),
    (2, 1, -4)
]

bellmanFord(3, edges, 0)