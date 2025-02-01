import math
from Shape.point import Point
from Shape.line import Line

class Shape:
    """
    Esta clase representa una figura en un espacio bidimensional o
    tridimensional. La figura puede ser un triángulo o un rectángulo.
    Específicamente se definen las siguientes figuras:
    Triángulo: 
    - Equilátero: todos sus lados son iguales.
    - Isósceles: dos o tres lados son iguales.
    - Escaleno: todos sus lados son diferentes.
    - Tetraedro Trirrectángulo: tetraedro donde los tres ángulos de las 
    caras que convergen en un vértice son ángulos rectos
    Rectángulo:
    - Cuadrado: todos sus lados son iguales.
    """

    def vertices(self) -> list[Point]:
        """
        Devuelve los vértices de la figura.
        """
        raise NotImplementedError("Este método debe ser redefinido en " 
                                "las clases hijas.")

    def edges(self) -> list[Line]:
        """
        Devuelve las aristas de la figura.
        """
        raise NotImplementedError("Este método debe ser redefinido en " 
                                "las clases hijas.")

    def inner_angles(self) -> list[float]:
        """
        Devuelve los ángulos internos de la figura.
        """
        raise NotImplementedError("Este método debe ser redefinido en " 
                                "las clases hijas.")

    # Este método determina si una figura es regular
    def is_regular(self) -> bool:
        """
        Determina si una figura es regular.
        Para aprovechar el polimorfismo, este método debe ser
        implementado por las clases que heredan de Shape.
        """
        raise NotImplementedError("Este método debe ser redefinido en " 
                                "las clases hijas.")
    
    def compute_area(self) -> float:
        raise NotImplementedError("Este método debe ser redefinido en " 
                                "las clases hijas.")

    def compute_perimeter(self) -> float:
        raise NotImplementedError("Este método debe ser redefinido en " 
                                "las clases hijas.")

    def compute_inner_angles(self):
        raise NotImplementedError("Este método debe ser redefinido en " 
                                "las clases hijas.")
    
    def __str__(self):
        raise NotImplementedError("Este método debe ser redefinido en " 
                                "las clases hijas.")
    