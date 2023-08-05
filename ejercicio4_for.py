#Encontrar el menor valor de un conjunto de numeros dados.

n = int(input("Ingrese el número de valores a asignar: "))

menor_num = 1000000

for i in range (1, n + 1):
  num_asig = int(input(f"Ingrese el valor {i}: "))
  
  if menor_num > num_asig:
    menor_num = num_asig
    
print(f"El menor valor es {menor_num}")
