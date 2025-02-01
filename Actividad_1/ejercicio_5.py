'''
Escribir una función que reciba una lista de string y retorne unicamente 
aquellos elementos que tengan los mismos caracteres. e.g. entrada: 
["amor", "roma", "perro"], salida ["amor", "roma"]
'''

def mismo_caracter(lista):
    resultado = []
    for palabra in lista:
        for otra_palabra in lista:
            '''
            Primero se compara si son diferentes indices y luego se comprueba 
            si tiene los mismos caracteres.
            '''
            if palabra != otra_palabra and sorted(palabra) == sorted(otra_palabra):
                resultado.append(palabra)
    # set() elimina elementos duplicados en la salida
    return list(set(resultado))  

opcion = True
while opcion:
    lista = []

    try:
        maximo = int(input("¿Cuántas palabras desea ingresar en la lista? "))
        if maximo < 2:
            raise ValueError("Debe ingresar al menos dos palabras.")
    except ValueError as e:
        print(f"Error: {e}")
        continue

    for i in range(maximo):
        while True:
            palabra = input(f"Ingrese la palabra {i + 1}: ").strip()
            if palabra:
                lista.append(palabra)
                break
            print("Error: No puede ingresar una palabra vacía.")

    resultado = mismo_caracter(lista)
    print("La lista de palabras ingresada es:", lista)
    if resultado:
        print("La lista de palabras que tienen los mismos caracteres es:", resultado)
    else:
        print("No hay palabras con los mismos caracteres en la lista.")

    opcion = input("¿Desea comprobar otra lista de palabras? (s/n): ").lower()
    if opcion!= 's':
        opcion = False