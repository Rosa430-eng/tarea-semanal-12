class Usuario:
    """
    Representa a un usuario registrado en la biblioteca.
    """

    def __init__(self, nombre, id_usuario):

        self.__nombre = nombre
        self.__id_usuario = id_usuario

        # Lista obligatoria para préstamos
        self.__libros_prestados = []

    # =====================
    # GETTERS
    # =====================

    def obtener_id(self):
        return self.__id_usuario

    def obtener_nombre(self):
        return self.__nombre

    def obtener_libros(self):
        return self.__libros_prestados

    # =====================
    # GESTIÓN DE PRÉSTAMOS
    # =====================

    def agregar_prestamo(self, libro):
        self.__libros_prestados.append(libro)

    def devolver_libro(self, isbn):

        for libro in self.__libros_prestados:
            if libro.obtener_isbn() == isbn:
                self.__libros_prestados.remove(libro)
                return libro

        return None

    def __str__(self):
        return f"Usuario: {self.__nombre} | ID: {self.__id_usuario}"