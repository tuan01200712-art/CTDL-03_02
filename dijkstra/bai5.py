INF = float('inf')

# Đồ thị vô hướng G2
graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 3), ('B', 2), ('D', 3)],
    'D': [('B', 5), ('C', 3), ('E', 4)],
    'E': [('D', 4)]
}

def dijkstra(graph, start):
    dist = {v: INF for v in graph}
    visited = {v: False for v in graph}

    dist[start] = 0

    for _ in range(len(graph)):

        u = None
        min_dist = INF

        # Chọn đỉnh chưa xét có khoảng cách nhỏ nhất
        for v in graph:
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v

        if u is None:
            break

        visited[u] = True

        # Relax các cạnh kề
        for neighbor, weight in graph[u]:
            if not visited[neighbor]:
                if dist[u] + weight < dist[neighbor]:
                    dist[neighbor] = dist[u] + weight

    return dist

result = dijkstra(graph, 'A')

print("Khoảng cách ngắn nhất từ A:")
for city, distance in result.items():
    print(f"A -> {city} = {distance}")