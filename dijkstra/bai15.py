import heapq

def dijkstra_grid(grid):

    rows = len(grid)
    cols = len(grid[0])

    INF = float('inf')

    dist = [[INF] * cols for _ in range(rows)]

    directions = [
        (-1, 0),  # lên
        (1, 0),   # xuống
        (0, -1),  # trái
        (0, 1)    # phải
    ]

    dist[0][0] = grid[0][0]

    heap = [(grid[0][0], 0, 0)]

    while heap:

        cost, x, y = heapq.heappop(heap)

        if cost > dist[x][y]:
            continue

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < rows and 0 <= ny < cols:

                new_cost = cost + grid[nx][ny]

                if new_cost < dist[nx][ny]:

                    dist[nx][ny] = new_cost

                    heapq.heappush(
                        heap,
                        (new_cost, nx, ny)
                    )

    return dist[rows - 1][cols - 1]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

result = dijkstra_grid(grid)

print("Chi phí nhỏ nhất =", result)