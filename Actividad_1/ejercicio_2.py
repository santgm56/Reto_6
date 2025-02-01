'''
Realice una función que permita validar si una palabra es un palíndromo. 
Condición: No se vale hacer slicing para invertir la palabra y verificar 
que sea igual a la original.
'''
def es_palindromo(palabra):
    ''' 
    Función que recibe una palabra y devuelve True si es un palíndromo 
    y False si no lo es.
    
    Se eliminan los espacios y se convierte la palabra a minúsculas.
    '''
    if not isinstance(palabra, str):
        raise TypeError("La palabra ingresada no es un string.")
    
    palabra = palabra.replace(' ', '').lower()
        
    if not palabra.isalnum():
        raise ValueError("Solo se permite letras o números.")
    
    for i in range(len(palabra)):  # Se recorre la palabra para comparar las letras.
        if palabra[i] != palabra[-i-1]:
            return False
    return True

opcion = True
while opcion:
    # Se solicita al usuario que ingrese una palabra.
    palabra = input("Ingrese una palabra: ")
    try:
        # Se verifica si la palabra es un palíndromo y 
        # se imprime el resultado.
        if es_palindromo(palabra):
            print(f"{palabra} es un palíndromo.")
        else:
            print(f"{palabra} no es un palíndromo.")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
    finally:
        # Se pregunta si el usuario quiere ingresar otra palabra.
        opcion = input("¿Desea ingresar otra palabra? (s para Sí/ Cualquier otra tecla para No): ").lower()
        if opcion != 's':
            opcion = False
