# for

# for element in range(1, 21):
#   print(element)

from itertools import product


list = [20, 21, 22, 23, 24, 25]
for element in list:
  print(element)

tupla = ('manzana', 'pera', 'bananas')
for element in tupla:
  print(element)

product = {
  "camisa": 20,
  "precio": 36,
  "stock": 23
}

for element in product:
  print(element, '=>', product[element])

for key in product:
  print(key, '=>', product[key])

for key, value in product.items():
  print(key, '=>', value)

personas = [
  {
    'nombre': 'Kat',
    'edad': 26
  },
  {
    'nombre': 'Ramon',
    'edad': 40
  },
  {
    'nombre': 'Zule',
    'edad': 23
  }
]

for persona in personas:
  print('nombre =>', persona['nombre'])