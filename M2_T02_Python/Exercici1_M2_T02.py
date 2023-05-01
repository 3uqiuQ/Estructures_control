
print('\n')
nota = float(input('Quina nota has tret a l\'examen?  '))
nota = round(nota, 2)

if nota >= 0 and nota < 5:
    print(str(nota) + '. Malauradament, has suspés l\'examen.')
elif nota >= 5 and nota < 7:
    print(str(nota) + '. Has aprovat l\'examen.')
elif nota >= 7 and nota < 9:
    print(str(nota) + '. Molt bé! Tens un notable!!')
elif nota >= 9:
    print(str(nota) + '. L\'enhorabona !!! Excel.lent !!!')
else:
    print('Si us plau, introdueix de nou la nota. NO pot ser un numero negatiu.')