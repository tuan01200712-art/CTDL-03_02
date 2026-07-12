def remove_if(arr, condition):
    write = 0

    for read in range(len(arr)):
        if not condition(arr[read]):
            arr[write] = arr[read]
            write += 1

    del arr[write:]
    return arr


a = [1, 2, 3, 4, 5, 6]
remove_if(a, lambda x: x % 2 == 0)

print(a)