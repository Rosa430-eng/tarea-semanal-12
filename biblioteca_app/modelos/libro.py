class Libro:
    """
    Representa un libro dentro del catálogo de la biblioteca.
    """

    def __init__(self, titulo, autor, categoria, isbn):

        # Tupla obligatoria (inmutable)
        self.__info = (titulo, autor)

        self.__categoria = categoria
        self.__isbn = isbn
        self.__disponible = True

    # =====================
    # GETTERS
    # =====================

    def obtener_titulo(self):
        return self.__info[0]

    def obtener_autor(self):
        return self.__info[1]

    def obtener_categoria(self):
        return self.__categoria

    def obtener_isbn(self):
        return self.__isbn

    def esta_disponible(self):
        return self.__disponible

    # =====================
    # ESTADO DEL LIBRO
    # =====================

    def prestar(self):
        self.__disponible = False

    def devolver(self):
        self.__disponible = True

    def __str__(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"{self.__info[0]} - {self.__info[1]} | {self.__categoria} | ISBN:{self.__isbn} | {estado}"