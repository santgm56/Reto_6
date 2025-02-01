from Shape.point import Point

class Line:  
    """
    Representa una línea en un espacio bidimensional. La línea es 
    definida por dos puntos: x, y; que hereda de la clase Point.
    """
    def __init__(self, start, end, n: int = 2):
        # Verifica que los puntos sean instancias de la clase Point
        if not isinstance(start, Point) or not isinstance(end, Point):
            raise ValueError("Los puntos deben ser instancias de la "
                            "clase Point.") 
            
        # Atributos de clase Point
        self.__start = start
        self.__end = end
        self.__length: float = self.compute_length()

    # Setters and Getters of attributes class Points
    @property
    def start(self):
        return self.__start
        
    @start.setter
    def start(self, point_start: Point):
        if not isinstance(point_start, Point):
            raise TypeError("El punto de fin debe ser una instancia "
                            "de la clase Point.")
        self.__start = point_start
        self.__length = self.compute_length()

    @property
    def end(self):
        return self.__end
        
    @end.setter
    def end(self, point_end: Point):
        if not isinstance(point_end, Point):
            raise TypeError("El punto de fin debe ser una instancia "
                            "de la clase Point.")
        self.__end = point_end
        self.__length = self.compute_length()

    # Método que hereda de la clase Point y calcula la distancia 
    # entre los dos puntos
    def compute_length(self) -> float:
        return self.__start.compute_distance(self.__end)

    @property
    def length(self):
        return self.__length
    
    def __str__(self):
        return f"({self.start}) -> ({self.end})"