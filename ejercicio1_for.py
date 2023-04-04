#Un Zoólogo pretende determinar cuántos animales hay en las categorías de edades: menos de 5 años, y de 5 o más años. El zoológico todavía no está seguro del animal que va a estudiar. Si se decide por elefantes solo tomará una muestra de 5 de ellos; si se decide por jirafas, tomará 7 muestras y si son chimpancés tomará 8.


animal = input("Ingrese el animal a escoger: ")
print("\n RECUERDE QUE: \n Solo tomara muestra de 5 elefantes \n Solo tomara muestra de 7 jirafas \n solo tomara muestra de 8 chimpancés \n")
muestra = int(input("Confirme el numero de muestras del animal escogido: "))


elefantes = 5
jirafas = 7
chimpancés = 8
menores = 0
mayores = 0


if animal == "elefantes" or "jirafas" or "chimpances":
  for i in range(1, muestra + 1):
    edad = int(input(f"Ingresé la edad del animal {i}: "))
    if edad >= 5:
      mayores += 1
    elif edad < 5:
      menores += 1
        
    
print(f"\n Hay {mayores} {animal} mayores a 5 años")
print(f"\n Hay {menores} {animal} mayores a 5 años")