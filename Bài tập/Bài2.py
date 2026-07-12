def insertionsort(A):
    shift = 0 
    for i in range (1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
            shift += 1
        A[j + 1] = key
    return shift

A = [5, 2, 4, 6, 1, 3]
print("Mảng ban đầu:", A)
shifts = insertionsort(A)
print("Mảng sau khi sắp xếp:", A)
print("Số lần dịch chuyển:", shifts)