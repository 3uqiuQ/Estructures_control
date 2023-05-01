llista = [2,1,3,7,9,9,0,8,6,0,9,3,13,5,2]
nova_llista = []
print(type(llista))
print(llista, '\n')

i = 0
while i < len(llista):
    if llista[i] == i + 1:
        nova_llista.append(llista[i])
        i += 1
    else:
        i += 1

if nova_llista :
    print('Els números que coincideixen amb la seva posició son: {}'.format(nova_llista))
else:
    print('No hi ha cap número que coincideixi amb la seva posició\n')
