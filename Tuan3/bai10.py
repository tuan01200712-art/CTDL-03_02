def demshift(a):
    shift = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            shift += 1
            j -= 1
    return shift

def songhichthe(a):
    dem = 0     
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                dem += 1
    return dem

a = [2, 4, 1, 3]

print("So nghich the:", songhichthe(a))
print("So shift:", demshift(a.copy()))