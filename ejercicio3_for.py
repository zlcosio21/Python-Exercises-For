#En una empresa se requiere calcular el salario semanal en dólares decada uno de los n obreros que laboran en ella. El salario se obtiene dela siguiente forma: a) Si el obrero trabaja 40 horas o menos se le paga $20 por hora. b) Si trabaja más de 40 horas se le paga $20 por cada una de las primeras 40 horas y $25 por cada hora extra

cant_obreros = int(input("Ingrese la cantidad de obreros en la empresa: "))

for n in range(1, cant_obreros + 1):
    horas_obrero = int(input(f"Ingrese la cantidad de horas trabajadas del obrero {n}: "))

    if horas_obrero <= 40:
        salario_obrero = horas_obrero * 20
    elif horas_obrero > 40:
        salario_obrero = (40 * 20) + ((horas_obrero - 40) * 25) 

    print(f"El salario semanal del obrero {n} es de ${salario_obrero} dolares")
