def quick_sort (v,ini,fim):
    meio = (ini + fim ) // 2
    pivo = v[meio]
    i = ini
    j = fim

    while i<j:
        while v[i] < pivo:
            i +=1
    while v[j] > pivo:
        j -=1

    if i<=j:
        v[i], v[j] = v[j], v[i]
    i+= 1
    j -=1

    if j > ini:                 # inicio da recursao de subvetores
        quick_sort (v,ini,j)
    if i< fim:
        quick_sort (v,i,fim)
        

