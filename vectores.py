"""
vectores.py: modulo hecho para el manejo de vectores 
programa hecho por martina vermiglio mas 

tests unitarios globales:
>>> from algebra.vectores import Vector
>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2.0, 4.0, 6.0])
>>> v1 @ v2
32.0
>>> v1 = Vector([2, 1, 2])
>>> v2 = Vector([0.5, 1, 0.5])
>>> v1 // v2
Vector([1.0, 2.0, 1.0])
>>> v1 % v2
Vector([1.0, -1.0, 1.0])
>>> v1 // v2 + v1 % v2 == v1
True
"""

class Vector:
    """clase que define un vector de n componentes y sus operaciones"""

    def __init__(self, data):
        """constructor que inicializa el vector con una lista de valores"""
        self.data = [float(x) for x in data]

    def __len__(self):
        """devuelve la longitud del vector"""
        return len(self.data)

    def __getitem__(self, index):
        """permite acceder a los elementos por índice"""
        return self.data[index]

    def __repr__(self):
        """representacion textual del vector"""
        return f"Vector({self.data})"

    def __add__(self, other):
        """suma de dos vectores"""
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        """resta de dos vectores (necesario para el operador %)"""
        return Vector([a - b for a, b in zip(self, other)])

    def __eq__(self, other):
        """compara si dos vectores son iguales (necesario para el test final)"""
        return self.data == other.data

    def __mul__(self, other):
        """
        producto de hadamard (elemento a elemento) o por un escalar
        >>> from algebra.vectores import Vector
        >>> v1 = Vector([1, 2, 3])
        >>> v1 * 2
        Vector([2.0, 4.0, 6.0])
        """
        if isinstance(other, (int, float)):
            return Vector([a * other for a in self.data])
        return Vector([a * b for a, b in zip(self, other)])

    def __rmul__(self, other):
        """multiplicación por la derecha (escalar * vector)"""
        return self.__mul__(other)

    def __matmul__(self, other):
        """
        producto escalar de dos vectores usando el operador @
        >>> from algebra.vectores import Vector
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 @ v2
        32.0
        """
        return sum(a * b for a, b in zip(self, other))

    def __floordiv__(self, other):
        """
        devuelve la componente tangencial de self respecto a other
        fórmula: v1|| = ((v1 @ v2) / (v2 @ v2)) * v2
        """
        escalar = (self @ other) / (other @ other)
        return other * escalar

    def __mod__(self, other):
        """
        devuelve la componente normal de self respecto a other
        fórmula: v1_normal = v1 - v1||
        """
        return self - (self // other)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)