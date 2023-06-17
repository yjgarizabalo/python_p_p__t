# condicionales
if True:
  print("Ejecutar si es verdadero")

if False:
  print("Ejecutar si es falso")

'''
mascota = input("¿Cual es tu mascota favorita? ")

if mascota == 'perro':
  print("Te gusta levantarte temprano")

elif mascota == 'gato':
  print("Cuida tu cena")

elif mascota == 'pez':
  print("Eres de pueblo")
else:
  print("No tienes mascota, eres feliz")
'''

'''
inventario = int(input("Digita el stock => "))

if inventario >= 100 and inventario <= 1000:
  print("Inventario correcto")
else:
  print("Revisar inventario")
'''

numero = int(input("Ingrese un numero => "))
resultado = numero % 2

if (resultado == 0):
  print("Es un numero par")
else:
  print("Es un numero impar")