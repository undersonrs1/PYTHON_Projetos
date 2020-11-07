def insertion_sort(v):
    for i in range (1, len(v)):
        x = v[i]
        j = i-1
        while j>=0 and x< v[j]:
            v[j+1] = v[j]
            j -= 1
            v[j+1] = x

            
print()
b = [8,3,9,2,1,10,7,5,4,6]
print(b)
print()
a = insertion_sort(b)
print()
a = b
print(a)
print()


