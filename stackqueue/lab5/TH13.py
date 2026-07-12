def remove_duplicates(arr):
    seen = set()
    result = []

    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)

    return result


a = [3, 1, 3, 2, 1]
print(remove_duplicates(a))