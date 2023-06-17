import random

opcion = ('piedra', 'papel', 'tijera')

victoria_usario = 0
victoria_computadora = 0

rondas = 1


while True:
  user = input("Elige: Piedra, papel o tijera => ")
  user = user.lower()

  print("*" * 10)
  print("Rondas", rondas)
  print("*" * 10)

  print("usuario", victoria_usario)
  print("computadora", victoria_computadora)

  if not user in opcion:
    print("Esa opcion no es validad")
    continue

  opcion_computadora = random.choice(opcion)

  print("Opcion del usuario",  user)
  print("Opcion de la computadora", opcion_computadora)

  if user == opcion_computadora:
    print("Es un empate")
  elif user == 'piedra':
    if opcion_computadora.lower() == 'tijera' :
      print("Piedra le gana tijera")
      print("Usuario Gano!")
      victoria_usario += 1
    else:
      print("Papel gana a piedra")
      print("Computadora Gano!")
      victoria_computadora += 1
  elif user == 'papel':
    if opcion_computadora.lower() == 'piedra':
      print("Papel gana a tijera")
      print("Usuario Gano!")
      victoria_usario += 1
    else:
      print("tijera gana a papel")
      print("Computador Gano!")
      victoria_computadora += 1
  elif user == 'tijera':
    if opcion_computadora.lower() == 'papel':
      print("Tijera le gana a papel")
      print("Usuario Gano!")
      victoria_usario += 1
    else:
      print("Piedra gana a tijera")
      print("Computadora Gano!")
      victoria_computadora += 1
  if victoria_computadora == 2:
    print("El computador gana")
    break
  if victoria_usario == 2:
    print("El usario gana")
    break   
  rondas += 1