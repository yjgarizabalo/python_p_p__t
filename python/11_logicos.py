# operadores logicos
# and
print("AND")
print("True and True", True and True) 
print("True and False", True and False) 
print("False and True", False and True) 
print("False and False", False and False) 

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

inventario = input("Ingre el numero stack => ")
inventario = int(inventario)

print(inventario >= 100 and inventario <= 1000)

# or
print("OR")
print("True and True", True or True) 
print("True and False", True or False) 
print("False and True", False or True) 
print("False and False", False or False) 

rol = input("Ingres Rol => ")
print(rol == "admin" or rol == "seller")
