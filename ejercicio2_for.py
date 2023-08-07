#Calcular el promedio de edades de hombres, mujeres, y de todo un grupo de alumnos.

mujeres = int(input("Ingrese cuantas mujeres hay en el grupo: "))
hombres = int(input("Ingrese cuantas hombres hay en el grupo: "))

sum_mujeres = 0
sum_hombres = 0

for m in range(1, mujeres + 1):
  edad_mujeres = int(input(f"Ingrese la edad de la mujer {m}: "))
  sum_mujeres = sum_mujeres + edad_mujeres

for h in range(1, hombres + 1):
  edad_hombres = int(input(f"Ingrese la edad del hombre {h}: "))
  sum_hombres = sum_hombres + edad_hombres

promedio_mujeres = sum_mujeres / mujeres
promedio_hombres = sum_hombres / hombres
promedio_grupo = (sum_mujeres + sum_hombres) / (mujeres + hombres)

print(f"El promedio de las mujeres es de {round(promedio_mujeres, 2)}")
print(f"El promedio de los hombres es de {round(promedio_hombres, 2)}")
print(f"El promedio de todo el grupo de alumnos es {round(promedio_grupo, 2)}")
