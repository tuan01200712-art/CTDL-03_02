def common_elements(arr1, arr2):
    hash_set = set(arr1)

    result = []

    for item in arr2:
        if item in hash_set and item not in result:
            result.append(item)

    return result


arr1 = [1, 2, 3]
arr2 = [2, 3, 4]

print(common_elements(arr1, arr2))