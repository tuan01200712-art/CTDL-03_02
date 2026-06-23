def trangthaisaukbuoc(a):
    for i in range(1,k + 1):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1  
        a[j + 1] = key
    return a

a = [5,2,4,6,1,3]
k = int(input("Nhap k: "))
print(trangthaisaukbuoc(a))