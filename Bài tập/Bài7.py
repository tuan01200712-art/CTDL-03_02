def countSubarrays(A, S):
    prefix = 0
    count = 0
    hashMap = {0: 1}

    for num in A:
        prefix += num

        if prefix - S in hashMap:
            count += hashMap[prefix - S]

        if prefix in hashMap:
            hashMap[prefix] += 1
        else:
            hashMap[prefix] = 1

    return count


A = [3, 4, 7, 2, -3, 1, 4, 2]
S = 7

print("Số mảng con có tổng bằng", S, "là:", countSubarrays(A, S))