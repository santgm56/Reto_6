from Shape import (point, rectangle, square,
                isosceles, equilateral, scalene, trirectangle)

def get_point_from_user(prompt):
    """
    Solicita al usuario ingresar las coordenadas de un punto.
    """
    while True:
        try:
            x = float(input(f"Ingrese la coordenada x para {prompt}: "))
            y = float(input(f"Ingrese la coordenada y para {prompt}: "))
            return point.Point(x, y)
        except ValueError:
            print("Error: Las coordenadas deben ser números. Intente nuevamente.")

def get_positive_float_from_user(prompt):
    """
    Solicita al usuario ingresar un número positivo.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: El valor debe ser positivo. Intente nuevamente.")
            else:
                return value
        except ValueError:
            print("Error: Debe ingresar un número. Intente nuevamente.")

def main():
    print("Bienvenido a mi programa de Geometría del Reto 6 :)")

    while True:
        print("\nSeleccione la figura que desea crear:")
        print("1. Rectángulo")
        print("2. Cuadrado")
        print("3. Triángulo Isósceles")
        print("4. Triángulo Equilátero")
        print("5. Triángulo Escaleno")
        print("6. Triángulo Rectángulo")
        print("7. Salir")

        choice = input("Ingrese el número de la opción: ")

        if choice == "1":
            try:
                # Crear un rectángulo
                bottom_left = get_point_from_user("la esquina inferior izquierda")
                width = get_positive_float_from_user("Ingrese el ancho del rectángulo: ")
                height = get_positive_float_from_user("Ingrese la altura del rectángulo: ")
                rect = rectangle.Rectangle(bottom_left, width, height)
                print(rect)
            except Exception as e:
                print(f"Error al crear el rectángulo: {e}")

        elif choice == "2":
            try:
                # Crear un cuadrado
                bottom_left = get_point_from_user("la esquina inferior izquierda")
                side_length = get_positive_float_from_user("Ingrese la longitud del lado del cuadrado: ")
                sqr = square.Square(bottom_left, side_length)
                print(sqr)
            except Exception as e:
                print(f"Error al crear el cuadrado: {e}")

        elif choice == "3":
            try:
                # Crear un triángulo isósceles
                print("Ingrese los tres vértices del triángulo isósceles:")
                v1 = get_point_from_user("el primer vértice")
                v2 = get_point_from_user("el segundo vértice")
                v3 = get_point_from_user("el tercer vértice")
                isos = isosceles.Isosceles(v1, v2, v3)
                print(isos)
            except Exception as e:
                print(f"Error al crear el triángulo isósceles: {e}")

        elif choice == "4":
            try:
                # Crear un triángulo equilátero
                print("Ingrese los tres vértices del triángulo equilátero:")
                v1 = get_point_from_user("el primer vértice")
                v2 = get_point_from_user("el segundo vértice")
                v3 = get_point_from_user("el tercer vértice")
                equiltl = equilateral.Equilateral(v1, v2, v3)
                print(equiltl)
            except Exception as e:
                print(f"Error al crear el triángulo equilátero: {e}")

        elif choice == "5":
            try:
                # Crear un triángulo escaleno
                print("Ingrese los tres vértices del triángulo escaleno:")
                v1 = get_point_from_user("el primer vértice")
                v2 = get_point_from_user("el segundo vértice")
                v3 = get_point_from_user("el tercer vértice")
                scalen = scalene.Scalene(v1, v2, v3)
                print(scalen)
            except Exception as e:
                print(f"Error al crear el triángulo escaleno: {e}")

        elif choice == "6":
            try:
                # Crear un triángulo rectángulo
                print("Ingrese los dos catetos del triángulo rectángulo:")
                v1 = get_point_from_user("el primer cateto")
                v2 = get_point_from_user("el segundo cateto")
                tri_rect = trirectangle.Trirectangle(v1, v2)
                print(tri_rect)
            except Exception as e:
                print(f"Error al crear el triángulo rectángulo: {e}")

        elif choice == "7":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()