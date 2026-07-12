a = [2, 4, 6, 8]
x = 5

left = 0
right = len(a) - 1

found = False

while left <= right:
    mid = (left + right) // 2

    if a[mid] == x:
        found = True
        break

    elif a[mid] < x:
        left = mid + 1

    else:
        right = mid - 1

print(found)