def sapxepgiatrituyetdoi(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and abs(a[j]) > abs(key):
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


a = [-3, 1, -2, 2]

print(sapxepgiatrituyetdoi(a))