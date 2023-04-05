#En una empresa se requiere calcular el salario semanal en dólares de cada uno de los n obreros que laboran en ella. El salario se obtiene de la siguiente forma: a) Si el obrero trabaja 40 horas o menos se le paga $20 por hora. b) Si trabaja más de 40 horas se le paga $20 por cada una de las primeras 40 horas y $25 por cada hora extra.


n = int(input("Ingrese la cantidad de obreros: "))


for i in range(1, n + 1):
  num_horas = int(input(f"Ingrese la cantidad de horas trabajadas del obrero {i}: "))
  if num_horas <= 40:
    salario = num_horas * 20
    print(f"El salario semanal del trabajador {i} es de ${salario}")
  elif num_horas > 40:
    salario =  800 + (num_horas * 25) - 1000 
    print(f"El salario semanal del trabajador {i} es de ${salario}")