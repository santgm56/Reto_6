from Shape.shape import Shape, Line, Point, math

class InvalidTriangleError(Exception):
    """
    Excepción personalizada para errores en la creación de un 
    triángulo.
    """
    def __init__(self, message):
        super().__init__(f"Error en Triangle: {message}")

class Triangle(Shape):
    """Representa un triángulo en un espacio bidimensional."""
    
    def __init__(self, v1: Point, v2: Point, v3: Point):
        """Inicializa el triángulo con tres vértices."""
        if not all(isinstance(v, Point) for v in (v1, v2, v3)):
            raise InvalidTriangleError("""Todos los vértices deben ser 
                                    instancias de Point.""")
        
        self.__v1 = v1
        self.__v2 = v2
        self.__v3 = v3

        if not self.is_valid_triangle():
            raise InvalidTriangleError("""Los puntos dados no forman un 
                                    triángulo válido.""")
    
    def is_valid_triangle(self) -> bool:
        """Verifica si los puntos forman un triángulo válido usando la 
        desigualdad triangular y colinealidad."""
        a = Line(self.__v1, self.__v2).compute_length()
        b = Line(self.__v2, self.__v3).compute_length()
        c = Line(self.__v3, self.__v1).compute_length()

        # Verificar si los puntos son colineales usando 
        # determinantes (área == 0)
        area = abs(
            (self.__v1.x * (self.__v2.y - self.__v3.y) + 
            self.__v2.x * (self.__v3.y - self.__v1.y) + 
            self.__v3.x * (self.__v1.y - self.__v2.y)) / 2
        )
        if area == 0:
            return False

        # Verificar desigualdad triangular
        return (a + b > c) and (b + c > a) and (a + c > b)

    @property
    def vertices(self):
        """Devuelve los vértices del triángulo."""
        return [self.__v1, self.__v2, self.__v3]

    @property
    def edges(self) -> list[Line]:
        """Calcula los lados del triángulo."""
        v = self.vertices
        return [
            Line(v[0], v[1]),
            Line(v[1], v[2]),
            Line(v[2], v[0]),
        ]

    def is_regular(self):
        """Determina si el triángulo es regular."""
        return (all([line.compute_length() == 
                self.edges[0].compute_length() for line in self.edges]))
    
    def compute_perimeter(self):
        """Calcula el perímetro del triángulo."""
        return sum(edge.compute_length() for edge in self.edges)

    def compute_area(self):
        """Calcula el área del triángulo usando la fórmula de Herón."""
        a, b, c = (edge.compute_length() for edge in self.edges)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def compute_inner_angles(self):
        """
        Calcula los ángulos internos del triángulo usando 
        la ley del coseno.
        """
        a, b, c = (edge.compute_length() for edge in self.edges)

        angle_A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        angle_B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
        angle_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))

        return [round(angle, 6) for angle in [angle_A, angle_B, angle_C]]

    def __str__(self):
        """Devuelve una representación en string del triángulo."""
        vertices_str = ", ".join([
            f"({v.x}, {v.y})" 
            for v in self.vertices])
        edges_str = ", ".join([
            f"({e.start.x}, {e.start.y}) -> ({e.end.x}, {e.end.y})" 
            for e in self.edges
            ])

        return (
            f"Este triángulo tiene las siguientes especificaciones:\n"
            f"- Vértices: {vertices_str}\n"
            f"- Lados (aristas): {edges_str}\n"
            f"- Área: {self.compute_area()}\n"
            f"- Perímetro: {self.compute_perimeter()}\n"
            f"- Ángulos internos: {self.compute_inner_angles()}\n"
            f"- Es regular: {'Sí' if self.is_regular() else 'No'}"
        )