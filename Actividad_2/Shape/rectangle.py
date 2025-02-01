from Shape.shape import Shape, Line, Point, math

class InvalidRectangleError():
    """Excepción para errores al inicializar un rectángulo."""
    def __init__(self, message):
        super().__init__(f"Error en Rectangle: {message}")

class Rectangle(Shape):
    """
    Representa un rectángulo en un espacio bidimensional.
    Se puede definir de tres maneras:
    1. Dando la esquina inferior izquierda + ancho + alto.
    2. Dando el centro + ancho + alto.
    3. Dando dos esquinas opuestas.
    """
    def __init__(self, *args):
        try:
            if (
                len(args) == 3 
                and isinstance(args[0], Point) 
                and isinstance(args[1], (int, float))
                and isinstance(args[2], (int, float))
            ):  
                self.__init_from_bottom_left(*args)
            elif (
                len(args) == 3 
                and isinstance(args[0], Point) 
                and isinstance(args[1], (int, float)) 
                and isinstance(args[2], (int, float))
                ):
                self.__init_from_center(*args)
            elif (
                len(args) == 2 
                and isinstance(args[0], Point) 
                and isinstance(args[1], Point)
                ):
                self.__init_from_corners(*args)
            else:
                raise InvalidRectangleError("""Número de argumentos 
                                            inválido. Usa (bottom_left, 
                                            width, height), (center, 
                                            width, height) o 
                                            (bottom_left, top_right).
                                            """)

            if self.width <= 0 or self.height <= 0:
                raise InvalidRectangleError("El ancho y alto deben ser "
                                            "valores positivos.")
        except InvalidRectangleError as e:
            print(e)
            # Relanza la excepción para evitar la creación del objeto
            raise  

    def __init_from_bottom_left(self, bottom_left: Point, 
                                width: float, height: float):
        """
        Inicializa un rectángulo desde la esquina inferior izquierda.
        """
        self.bottom_left = bottom_left
        self.width = width
        self.height = height
        self.center = Point(bottom_left.x + width / 2, 
                            bottom_left.y + height / 2)

    def __init_from_center(self, center: Point, 
                        width: float, height: float):
        """Inicializa un rectángulo desde el centro."""
        self.center = center
        self.width = width
        self.height = height
        self.bottom_left = Point(center.x - width / 2, 
                                center.y - height / 2)

    def __init_from_corners(self, bottom_left: Point, top_right: Point):
        """Inicializa un rectángulo desde dos esquinas opuestas."""
        self.bottom_left = bottom_left
        self.width = top_right.x - bottom_left.x
        self.height = top_right.y - bottom_left.y
        self.center = Point(bottom_left.x + self.width / 
                            2, bottom_left.y + self.height / 2)

    def vertices(self):
        """Devuelve los vértices del rectángulo."""
        return [
            self.bottom_left,
            Point(self.bottom_left.x + self.width, self.bottom_left.y),
            Point(self.bottom_left.x + self.width, self.bottom_left.y + 
                self.height),
            Point(self.bottom_left.x, self.bottom_left.y + self.height),
        ]
    
    def edges(self):
        """Devuelve los lados del rectángulo."""
        v = self.vertices()
        return [
            Line(v[0], v[1]),
            Line(v[1], v[2]),
            Line(v[2], v[3]),
            Line(v[3], v[0]),
        ]
    
    def compute_area(self) -> float:
        """Calcula el área del rectángulo."""
        return self.width * self.height

    def compute_perimeter(self) -> float:
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.width + self.height)

    def compute_inner_angles(self):
        """Devuelve los ángulos internos en radianes."""
        return [round(math.pi / 2, 4)] * 4
    
    def is_regular(self) -> bool:
        """Determina si el rectángulo es regular."""
        return self.width == self.height
    
    def __str__(self):
        vertices_str = ", ".join([
            f"({v.x}, {v.y})" 
            for v in self.vertices()])
        edges_str = ", ".join([
            f"({e.start.x}, {e.start.y}) -> ({e.end.x}, {e.end.y})" 
            for e in self.edges()])

        return (
            f"Rectángulo:\n"
            f"- Esquina inferior izquierda: ({self.bottom_left.x}, {self.bottom_left.y})\n"
            f"- Dimensiones: Ancho = {self.width}, Alto = {self.height}\n"
            f"- Área: {self.compute_area()}\n"
            f"- Perímetro: {self.compute_perimeter()}\n"
            f"- Ángulos internos: {self.compute_inner_angles()}\n"
            f"- Es regular: {'Sí' if self.is_regular() else 'No'}\n"
            f"- Vértices: {vertices_str}\n"
            f"- Lados: {edges_str}"
        )

