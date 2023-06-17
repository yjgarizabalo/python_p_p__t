# tupla
numeros = (1,4,6,6,7)
string = ('Nico', 'Valentina', 'Kat', 'Laura')

# buscar
print(string.index('Kat'))
print(string.count('Nico'))

lista = list(string)

print(lista)
print(type(lista))

lista[0] = "Angie"
print(lista)

# cambiar una lista a una tupla
tupla = tuple(lista)
print(tupla)