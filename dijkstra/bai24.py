import heapq

def heuristic(a, b):

    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(start, goal):

    heap = []

    heapq.heappush(
        heap,
        (0, start)
    )

    g = {start:0}

    while heap:

        _, current = heapq.heappop(heap)

        if current == goal:
            return g[current]

        x,y = current

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        for dx,dy in directions:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < 5 and 0 <= ny < 5:

                new_g = g[current] + 1

                if (nx,ny) not in g or new_g < g[(nx,ny)]:

                    g[(nx,ny)] = new_g

                    f = new_g + heuristic(
                        (nx,ny),
                        goal
                    )

                    heapq.heappush(
                        heap,
                        (f,(nx,ny))
                    )

    return -1


print(
    astar(
        (0,0),
        (4,4)
    )
)