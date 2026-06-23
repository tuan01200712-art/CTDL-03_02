def demsolandichchuyen(a):
    dem = 0
    for i in range (1,len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1 
            dem += 1
        a[j + 1] = key
    return dem

a = [3,2,1]
print("So lan dich chuyen:", demsolandichchuyen(a))