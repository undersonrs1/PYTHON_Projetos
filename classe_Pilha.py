class Pilha():  # define classe Pilha e cria lista vazia
    def __init__(self):
        self.data = []

    def push(self, x):  # função que adiciona itens a lista, empilha
        self.data.append(x)

    def pop(self):  # função que remove itens da lista, desempilha
        if len(self.data) > 0:
            return self.data.pop(-1)

    def top(self):  # função que nos mostra ultimo valor inserido lista, topo lista
        if len(self.data) > 0:
            return self.data[-1]

    def empty(self):  # função que verifica se lista esta vazia
        return not len(self.data) > 0


p = Pilha()  # cria objeto na classe Pilha
num = 15  # define numero decimal que sera convertido para bin
while num > 0:  # enquanto num maior que 0
    resto = num % 2  # acumula resto da div em resto
    num = num // 2  # acumula em num a div inteira de num por 2
    p.push(resto)  # adiciona o resto na lista

while not p.empty():  # verifica se lista esta vazia
    print(p.pop())  # imprime os restos armazenados na seq ultimo para primeiro


