def canShip(W, K, capacity):
    trucks = 1
    current = 0

    for weight in W:
        if current + weight <= capacity:
            current += weight
        else:
            trucks += 1
            current = weight

    return trucks <= K


def splitGoods(W, capacity):
    trucks = []
    currentTruck = []
    currentWeight = 0

    for weight in W:
        if currentWeight + weight <= capacity:
            currentTruck.append(weight)
            currentWeight += weight
        else:
            trucks.append(currentTruck)
            currentTruck = [weight]
            currentWeight = weight

    trucks.append(currentTruck)
    return trucks


W = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 5

left = max(W)
right = sum(W)

while left < right:
    mid = (left + right) // 2

    if canShip(W, K, mid):
        right = mid
    else:
        left = mid + 1

capacity = left

print("Tải trọng tối thiểu:", capacity)

trucks = splitGoods(W, capacity)

for i in range(len(trucks)):
    print("Xe", i + 1, ":", trucks[i], "- Tổng =", sum(trucks[i]))