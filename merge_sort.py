def merge_sort(v,ini,fim):
    if ini<fim:
        meio = (ini + fim) // 2
        merge_sort = (v,ini,meio)
        merge_sort = (v, meio+1,fim)
        intercala = (v,ini,meio,fim)

def intercala(v,ini,meio,fim):
    L = v[ini:meio+1]
    R = v[meio+1:fim+1]

    L.append(999) #sentinela
    R.append(999) #sentinela

    i = 0
    j = 0

    for k in range (ini, fim+1):
        if L[i] <= R[j]:
            v[k] = L[i]
            i+= 1
    else:
        v[k] = R[j]
        j += 1
        

b = [10,5,3,4,2,8,1,9,7,6]
print()
print(b)
a = merge_sort (b,0,9)


print()
for c in range (0,9):
    print(b[c])
    print()



