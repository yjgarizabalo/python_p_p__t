# Diccionar

persona = {
  "nombre": "Kat",
  "apellido": "Donado",
  "hobies": ["Ver tv", "nana", "ir a playa"],
  "edad": 26,
  "cedula": 202304
}

print(persona)
persona['nombre'] = 'Paola'
persona['edad'] -= 2
persona['hobies'].append("sexo")
# del persona['cedula']
persona.pop('cedula')
print(persona)

print("Items")
print(persona.items())
print(persona.keys())
print(persona.values())

'''
Agregar un nuevo elemento al diccionario con la llave "twitter" y el valor "@nicobytes".
Actualizar el valor del elemento con la llave "name" con el valor "Felipe".
Eliminar el elemento del diccionario con la llave "age".
Imprimir una lista con las llaves del diccionario.
Imprimir una lista con los valores del diccionario.
'''