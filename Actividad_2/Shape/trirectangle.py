from Shape.triangle import Triangle, Point, math, InvalidTriangleError

class Trirectangle(Triangle):
    """
    Representa un triángulo rectángulo, que es un caso especial de 
    triángulo. Hereda de la clase Triangle, utilizando la fórmula de 
    Herón directamente.
    """

    def __init__(self, cateto_1: Point, cateto_2: Point):
        """
        Constructor para crear un triángulo rectángulo con dos catetos.
        Los puntos representan los catetos en un espacio bidimensional.
        """
        # Crear el tercer punto para formar el triángulo rectángulo
        hipotenusa_point = Point(cateto_1.x, cateto_2.y)

        # Llamar al constructor de la clase base con los 3 puntos
        super().__init__(cateto_1, cateto_2, hipotenusa_point)
        
        # Verificar si el triángulo es un triángulo rectángulo válido
        if not self.is_valid_triangle():
            raise InvalidTriangleError("""Los puntos dados no forman un 
                                    triángulo válido.""")
        if not self.is_right_triangle():
            raise InvalidTriangleError("""Este triángulo no es rectángulo,
                                    no cumple el teorema de Pitágoras.""")

    def is_right_triangle(self):
        """
        Verifica si el triángulo es un triángulo rectángulo.
        Ordena los lados para garantizar que el lado más largo sea la 
        hipotenusa.
        """
        # Calcular longitudes de los lados
        lengths = [edge.compute_length() for edge in self.edges]
        lengths.sort()  # Ordena las longitudes de menor a mayor

        # Teorema de Pitágoras: cateto_1^2 + cateto_2^2 = hipotenusa^2
        a, b, c = lengths  # a y b son catetos, c es la hipotenusa
        return math.isclose(a**2 + b**2, c**2, rel_tol=1e-9)

    def __str__(self):
        base_str = super().__str__()
        if self.is_right_triangle():
            base_str = base_str.replace("Este triángulo tiene:",
                                        "Este triángulo rectángulo tiene:")
            return f"{base_str} - Es un triángulo rectángulo válido."
        else:
            return f"{base_str} - No es un triángulo rectángulo válido."
