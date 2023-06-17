# CRUD => Crear listar actulizar y eliminar


numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(numeros[1])
numeros[-1] = 10
print(numeros)

numeros.append(200)
print(numeros)


numeros.insert(3, "elemento")
print(numeros)

numeros.insert(0, 'hola')
print(numeros)

tareas = ["Geraldine", "Kat", "Laura", "Katia", "Lizeth", "Angie", "Maria", "Gipesi"]

list_nueva = tareas + numeros
index = list_nueva.index('Katia')
list_nueva[index] = "Valentina"
print(list_nueva)

list_nueva.remove('Geraldine')
print(list_nueva)

list_nueva.pop()
print(list_nueva)

list_nueva.pop(3)
print(list_nueva)

list_nueva.reverse()
print(list_nueva)

numeros = [1, 2, 4, 5, 0]
numeros.sort()
print(numeros)

letras = ['b', 'c', 'x', 'm', 'a']
letras.sort()
print(letras)