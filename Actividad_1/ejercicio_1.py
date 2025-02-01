'''
Crear una función que realice operaciones básicas (suma, resta, 
multiplicación, división) entre dos números, según la elección del 
usuario, la forma de entrada de la función será los dos operandos y el 
caracter usado para la operación. entrada: (1,2,"+"), salida (3).
'''

def operaciones(x, y, operador): 
    '''
    Función que recibe dos números y una operación y devuelve el  
    resultado de la operación.
    '''
    try: # Se intenta realizar la operación correspondiente.
        if operador == "+":
            return (x + y, y)
        elif operador == "-": 
            return (x - y, y)
        elif operador == "*":
            return (x * y, y)
        elif operador == "/":
            if y == 0:
                raise ZeroDivisionError("No se puede dividir entre cero.")
            return (x / y, y)
        else:
            raise ValueError("Operación no válida. Use +, -, * o /.")
    except ZeroDivisionError as e:
        print(e)
        new_y = input("Ingrese un número diferente de cero: ")
        # Llamada recursiva con el nuevo valor de y
        return operaciones(x, float(new_y), operador)
    except ValueError as e:
        print(e)
        return (None, y)

opcion = True
while opcion: # Ciclo que permite realizar varias operaciones.
    try: # Se intenta comprobar que los valores ingresados son números.
        x = float(input("Ingrese el primer número: "))
        y = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Debe ingresar un número.")
        continue
    
    # Se pregunta al usuario qué operación quiere realizar.
    operacion = input("Ingrese la operación que deseas realizar (+, -, *, /): ")
    # Se llama a la función operaciones para obtener el resultado de la operación.
    resultado, new_y = operaciones(x, y, operacion) 
    if resultado is not None: # Se comprueba que el tipo de operación sea válida.
        print(f"El resultado de la operación {x} {operacion} {new_y} es : {resultado}")

    # Se pregunta al usuario si desea realizar otra operación.
    opcion = input("¿Desea realizar otra operación? (s para Sí/ Cualquier otra tecla para No): ").lower() 
    if opcion != 's':
        opcion = False
