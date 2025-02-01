from Shape.rectangle import Rectangle, Point, InvalidRectangleError

class InvalidSquareError(InvalidRectangleError):
    """Excepción para errores en la inicialización de un cuadrado."""
    def __init__(self, message):
        super().__init__(f"Error en Square: {message}")

class Square(Rectangle):
    """
    Clase que representa un cuadrado, un caso especial de un rectángulo 
    donde el ancho y la altura son iguales.
    """

    def __init__(self, bottom_left: Point, side_length: float):
        """
        Inicializa el cuadrado con la esquina inferior izquierda y el lado.
        """
        if not isinstance(bottom_left, Point):
            raise InvalidSquareError("""El punto inferior izquierdo debe 
                                    ser una instancia de Point.""")
        
        if not isinstance(side_length, (int, float)) or side_length <= 0:
            raise InvalidSquareError("""El lado del cuadrado debe ser un 
                                    número positivo.""")
        
        super().__init__(bottom_left, side_length, side_length)

    def compute_area(self):
        """Calcula el área del cuadrado."""
        return self.width ** 2
    
    def __str__(self):
        """Reutiliza la lógica del método __str__ de Rectangle pero 
        ajusta el encabezado."""
        rect_str = super().__str__()
        return rect_str.replace("Rectángulo", "Cuadrado")