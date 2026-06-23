def binarysearch(a,x, left, right):
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left

def binaryinsertionsort(a):
    for i in range(1, len(a)):
        key = a[i]
        pos = binarysearch(a, key, 0, i - 1)
        j = i - 1
        while j >= pos:
            a[j + 1] = a[j]
            j -= 1
        a[pos] = key
    return a 

a = [5, 2, 4, 6, 1, 3]
print(binaryinsertionsort(a))