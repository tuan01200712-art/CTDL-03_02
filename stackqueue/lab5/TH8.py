def remove_even(arr):
    write = 0

    for read in range(len(arr)):
        if arr[read] % 2 != 0:
            arr[write] = arr[read]
            write += 1

    del arr[write:]
    return arr


a = [1, 2, 3, 4, 5, 6, 7, 8]
print("Ban đầu:", a)

remove_even(a)

print("Sau khi xóa số chẵn:", a)