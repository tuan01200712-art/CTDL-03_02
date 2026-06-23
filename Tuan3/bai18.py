def chenphantuphai_sangtrai(a):
    sosanh = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            sosanh += 1
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key
    return sosanh 

def chenphantutrai_sang_phai(a):
    sosanh = 0
    for i in range(len(a) - 2, -1, -1):
        key = a[i]
        j = i + 1
        while j < len(a):
            sosanh += 1
            if a[j] < key:
                a[j - 1] = a[j]
                j += 1
            else:
                break
        a[j - 1] = key
    return sosanh

a1 = [1, 2, 3, 4, 6, 5]
a2 = a1.copy()

print("Phai -> Trai:", chenphantuphai_sangtrai(a1))
print("Trai -> Phai:", chenphantutrai_sang_phai(a2))