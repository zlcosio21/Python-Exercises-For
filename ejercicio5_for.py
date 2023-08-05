#En un supermercado una ama de casa pone en su carrito los artículos que va tomando de los estantes. La señora quiere asegurarse de que el  cajero le cobre bien lo que ella ha comprado, por lo que cada vez que toma un articulo anota su precio junto con la cantidad de artículos iguales que ha tomado y determina cuánto dinero gastará en ese artículo; a esto le suma lo que irá gastando en los demás artículos, hasta que decide que ya tomó todo lo que necesitaba. Ayúdele a esta señora a obtener el total de su compra

total_compra = []

articulos_a_comprar = int(input("Ingrese la cantidad de articulos a comprar: "))

for i in range(1, articulos_a_comprar + 1):
    articulo = input(f"Agregue el articulo {i} al carrito: ")
    precio  = int(input(f"Anote el precio del articulo {articulo}: "))
    cant_articulo = int(input(f"Ingrese la cantidad a comprar del articulo {articulo}: "))

    total_articulo = cant_articulo * precio
    total_compra.append(total_articulo)
    print(f"Gastara ${total_articulo} en la compra del articulo {articulo}")

print(f"El total de la compra es ${sum(total_compra)}")