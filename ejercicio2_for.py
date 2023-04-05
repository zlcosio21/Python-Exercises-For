#Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos.


grupo = int(input("Ingrese la cantidad de alumnos del grupo: "))
hombres = int(input("Ingrese la cantidad de hombres del grupo: "))
mujeres = int(input("Ingrese la cantidad de mujeres del grupo: "))


edad_hombres = 0
edad_mujeres = 0


if hombres and mujeres > grupo:
  print("Por favor ingrese la imformacion correctamente")


if hombres and mujeres <= grupo:
  for i in range(1, hombres + 1):
    edad_hombre = int(input(f"Ingrese la edad del hombre {i}: "))
    edad_hombres = edad_hombres + edad_hombre

    
if hombres and mujeres <= grupo:
  for e in range(1, mujeres + 1):
    edad_mujer = int(input(f"Ingrese la edad de la mujer {e}: "))
    edad_mujeres = edad_mujeres + edad_mujer


prom_grupo = (edad_hombres + edad_mujeres) / grupo
prom_hombres = edad_hombres / hombres
prom_mujeres = edad_mujeres / mujeres


print(f"El promedio del grupo de alumnos es de {prom_grupo}")
print(f"El promedio de los hombres es de {prom_hombres}")
print(f"El promedio de las mujeres es de {prom_mujeres}")