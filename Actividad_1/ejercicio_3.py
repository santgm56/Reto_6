'''
Escribir una función que reciba una lista de números y devuelva solo aquellos 
que son primos. La función debe recibir una lista de enteros y retornar solo 
aquellos que sean primos.
'''

def es_primo(lista):
    primos = []
    for numero in lista:
        if numero > 1:
            '''
            Comprobar si el número es primo verificando que no sea divisible por 
            ningún número entre 2 y el número - 1.
            '''
            for i in range(2, numero):
                if (numero % i) == 0:
                    break
            else:
                primos.append(numero)
    return primos

opcion = True
while opcion:
    lista = []
    try:
        maximo = int(input("¿Cuántos números desea ingresar en la lista? "))
        if maximo <= 0:
            raise ValueError("Debe ingresar un número mayor que cero.")
    except ValueError as e:
        print(f"Error: {e}")
        continue
    for i in range(maximo):
        while True:
            try:
                numero = int(input("Ingrese un número: "))
                lista.append(numero)
                break
            except ValueError:
                print(f"Error: Debe ingresar un número entero.")
    
    primos = es_primo(lista)
    primos.sort()
    print(f"Los números primos de la lista son: {primos}")

    opcion = input("¿Desea comprobar otra lista de números? (s/n): ").lower()
    if opcion != 's':
        opcion = False