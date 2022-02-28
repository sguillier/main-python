import openpyxl

book = openpyxl.load_workbook('test.xlsx')

hoja = book.active

hoja['A1'] = 'Hello World'

celdas = hoja['A1':'C3']

for fila in celdas:
    for celda in fila:
        print(celda.value)


book.save('test.xlsx')