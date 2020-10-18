s = 0
soma = 0
while True:
    num = int(input('Digite um número : '))
    if num == 999:
        break
    s += 1
    soma += num

print(f'Você digitou {s} números e a somatória deles é {soma}')
