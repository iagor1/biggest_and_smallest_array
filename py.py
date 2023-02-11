def FazLista(c=0):
   # primeiro argumento dita o tamanho da lista
    n = []
    for i in range(0, c):
        o = int(input('digite os elementos da lista : '))
        n.append(o)
    print(*n)
    return n

print('digite o tamanho da lista')
c = int(input())
l = FazLista(c)
print(l)

def MaiorElemento(lista):
    a = maior = 0
    for i in range(len(lista)):
        if lista[i] > lista[maior]:
            maior = i
    a = lista[maior]
    print('maior elemento ',a)



def MenorElemento(lista):

    
    a = menor = 0
    for i in range(len(lista)):
        if lista[i] < lista[menor]:
            menor = i
    a = lista[menor]
    print('menor elemento ',a)

MaiorElemento(l)
MenorElemento(l)