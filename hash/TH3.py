def count_frequency(arr):
    hash_table = {}

    for item in arr:
        if item in hash_table:
            hash_table[item] += 1
        else:
            hash_table[item] = 1

    return hash_table


arr = ["a", "b", "a", "c", "a"]

result = count_frequency(arr)

print(result)