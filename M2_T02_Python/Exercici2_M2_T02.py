
print('\n')
primer = int(input('Introdueix el primer número:  '))
segon = int(input('Introdueix un altre número:  '))

if type(primer) != int or type(segon) != int:
    print('Por favor, los números han de ser enteros.')
else:
    if primer > segon:
        print('El primer número: ({}) es mayor que el segón ({}).'.format(primer, segon))
    if segon > primer:
        print('El segón número: ({}) es mayor que el primer ({}).'.format(segon, primer))
    if primer == segon:
        print('Els dos números son iguals. ({} i {}, son el mateix número).'.format(primer, segon))

