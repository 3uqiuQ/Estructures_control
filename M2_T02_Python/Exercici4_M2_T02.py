

lista = [2,4,5,7,3,9,9,3,7,6,4,2]
print(type(lista))
print (lista, '\n')
i = 0
j = len(lista) -1
while i < j:
    if lista[i] == lista[j]:
        i +=1
        j -=1
    else:
        print('La lista NO es simétrica.')
        break
else:
    print('La lista es simétrica.')
