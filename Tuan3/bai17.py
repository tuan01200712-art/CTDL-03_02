def demshift(a):
    shift = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            shift += 1
            j -= 1
        a[j + 1] = key

    return shift   
 
a = [1, 2, 4, 3, 5]

print("Mang sau sap xep:", a)
print("So lan dich chuyen:", demshift(a))