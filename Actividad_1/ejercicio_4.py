'''
Escribir una función que reciba una lista de números enteros y retorne 
la mayor suma entre dos elementos consecutivos.
'''
def maxima_suma_consecutivos(lista):
    """
    Función que recibe una lista de números enteros y retorna
    la mayor suma entre dos elementos consecutivos.
    """
    if len(lista) < 2:
        raise ValueError("La lista debe contener al menos dos números.")

    max_suma = lista[0] + lista[1]  # Iniciar con la primera suma válida
    indice_1, indice_2 = 0, 1

    for i in range(len(lista) - 1):
        suma = lista[i] + lista[i + 1]
        if suma > max_suma:
            max_suma = suma
            indice_1, indice_2 = i, i + 1

    return max_suma, indice_1, indice_2


opcion = True
while opcion:
    lista = []

    try:
        maximo = int(input("¿Cuántos números desea ingresar en la lista? "))
        if maximo < 2:
            raise ValueError("Debe ingresar al menos dos números.")
    except ValueError as e:
        print(f"Error: {e}")
        continue

    for i in range(maximo):
        while True:
            try:
                numero = int(input(f"Ingrese el número {i + 1}: "))
                lista.append(numero)
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")

    try:
        max_sum, indice_1, indice_2 = maxima_suma_consecutivos(lista)
        print("La lista de números ingresada es:", lista)
        print(f"La mayor suma entre dos elementos consecutivos, los cuales son: {lista[indice_1]} + {lista[indice_2]}, es: {max_sum}")
    except ValueError as e:
        print(f"Error: {e}")
    opcion = input("¿Desea comprobar otra lista de números? (s/n): ").lower()
    if opcion != 's':
        opcion = False
