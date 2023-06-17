# NOT operador logico
from traceback import print_tb


print(not True)

print("NOT AND")
print("not True and True", not (True and True)) 
print("not True and False", not (True and False)) 
print("not False and True", not (False and True)) 
print("not False and False", not (False and False)) 

inventario = input("Ingre el numero stack => ")
inventario = int(inventario)

print(not (inventario >= 100 and inventario <= 1000))