# String
nombre = "Jesus"
apellido = "Ruiz"

nombre_completo = nombre + " " + apellido

print("su nombre es:", nombre_completo)

quote = "I'm Jesus"
print(quote)

quote2 = "Ella dijo 'Hola amigos'"
print(quote2)

# formatos

plantilla = "Hola, mi nombre es " + nombre + " y mi apellido es " + apellido 
print(plantilla)

plantilla2 = "Hola, mi nombre es {} y mi apellido es {}".format(nombre, apellido)
print(plantilla2)

plantilla3 = f"Hola, mi nombre es {nombre} y mi apellido es {apellido}".format(nombre,apellido)
print(plantilla3)