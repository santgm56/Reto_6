from Shape.triangle import Triangle, Point, math, InvalidTriangleError

class Equilateral(Triangle):
    """Clase para el triángulo equilátero."""
    def __init__(self, v1: Point, v2: Point, v3: Point):
        super().__init__(v1, v2, v3)
        if not self.is_valid_triangle():
            raise InvalidTriangleError("""Los puntos dados no forman un 
                                    triángulo válido.""")
        if not self.is_equilateral():
            raise InvalidTriangleError("Este triángulo no es equilátero.")

    def is_equilateral(self):
        """Determina si el triángulo es equilátero comparando la longitud
        de todos sus lados."""
        edge_lengths = [edge.compute_length() for edge in self.edges]
        return math.isclose(edge_lengths[0], 
                            edge_lengths[1], rel_tol=1e-9) and \
            math.isclose(edge_lengths[1], 
                        edge_lengths[2], rel_tol=1e-9) and \
            math.isclose(edge_lengths[0], edge_lengths[2], rel_tol=1e-9)
    
    """Sobrescribe el cálculo de área para evitar cálculos si no 
    es equilatero."""
    def inner_angles(self):
        if self.is_equilateral():
            return super().inner_angles()
        else:
            return [0, 0, 0]

    def compute_perimeter(self):
        if self.is_equilateral():
            return super().compute_perimeter()
        else:
            return 0
    
    def compute_area(self):
        if self.is_equilateral():
            return super().compute_area()
        else:
            return 0  

    def __str__(self):
        base_str = super().__str__() 
        # Verifica si es equilátero y ajusta la cadena de salida
        if self.is_equilateral():
            base_str = base_str.replace("Este triángulo tiene:", 
                                        "Este triángulo equilátero tiene:")
            return f"{base_str} - Es un triángulo equilátero."
        else:
            return f"{base_str} - No es un triángulo equilátero."