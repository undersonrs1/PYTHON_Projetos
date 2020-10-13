def primo(num):
    i=2
    while i<num:
        if num %i == 0:
            break
        i += 1
        return i == num

for n in range(2,100):
    if not primo(n):
        continue
    print(n)
    