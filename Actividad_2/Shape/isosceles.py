from Shape.triangle import Triangle, Point, InvalidTriangleError

class Isosceles(Triangle):
    """Clase para el triángulo isósceles."""
    def __init__(self, v1: Point, v2: Point, v3: Point):
        super().__init__(v1, v2, v3)
        if not self.is_valid_triangle():
            raise InvalidTriangleError("""Los puntos dados no forman un 
                                    triángulo válido.""")
        if not self.is_isosceles():
            raise InvalidTriangleError("Este triángulo no es isósceles.")

    def is_isosceles(self):
        """Determina si el triángulo es isósceles."""
        edges = [edge.compute_length() for edge in self.edges]
        return (edges[0] == edges[1] 
            or edges[1] == edges[2] or edges[2] == edges[0])
    
    def __str__(self):
        base_str = super().__str__()
        if self.is_isosceles():
            base_str = base_str.replace(
                "Este triángulo tiene:",
                "Este triángulo isósceles tiene:"
            )
            return f"{base_str} - Es un triángulo isósceles."
        else:
            return f"{base_str} - No es un triángulo isósceles."