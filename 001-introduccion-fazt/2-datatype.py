
# string
print('Hola Mundo')
print("Hola Mundo")
print('''Hola Mundo''')
print("""Hola Mundo""")
print(type('Hola Mundo'))

# integer
print(type(5))

# float
print(type(5.5))

# Boolean
False
True

# List
[1, 2, 3, True, False, 'Hola Mundo']

# Tuple  # Similar a List Pero Estos Datos No Pueden Cambiar
(1, 2, 3, True, False, 'Hola Mundo')

# Dictionary
print(type({
    "nombre": "Juan",
    "apellido": "Perez"
}))


print('Estoy aqui .................................................')
temp = {
    "nombre": "Juan",
    "apellido": "Perez"
}
print(temp)
print(temp["nombre"])


print('Estoy aqui 2 +++++++++++++++++++++++++++++++++++++++++++++++++')
temp = {
    "tick1": "tick1 CI Equity",
    "tick2": "tick2 CI Equity",
    "tick3": "tick3 CI Equity",
}
print(temp)
print(temp["tick1"])

try:
    temp["t"]
except:
    print("ticket no asignado")


#NoneType
print(type(None))