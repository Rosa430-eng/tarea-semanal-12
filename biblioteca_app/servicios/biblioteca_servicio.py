from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    """
    Contiene toda la lógica del negocio de la biblioteca.
    """

    def __init__(self):

        # Diccionario obligatorio
        # clave = ISBN
        # valor = objeto Libro
        self.catalogo = {}

        # Usuarios registrados
        self.usuarios = {}

        # Set obligatorio para IDs únicos
        self.ids_usuarios = set()

    # =====================
    # LIBROS
    # =====================

    def agregar_libro(self, titulo, autor, categoria, isbn):

        if isbn in self.catalogo:
            print(" El ISBN ya existe")
            return

        libro = Libro(titulo, autor, categoria, isbn)

        self.catalogo[isbn] = libro

        print(" Libro agregado al catálogo")

    def eliminar_libro(self, isbn):

        if isbn in self.catalogo:
            del self.catalogo[isbn]
            print("Libro eliminado")
        else:
            print("Libro no encontrado")

    # =====================
    # USUARIOS
    # =====================

    def registrar_usuario(self, nombre, id_usuario):

        if id_usuario in self.ids_usuarios:
            print(" ID ya registrado")
            return

        usuario = Usuario(nombre, id_usuario)

        self.usuarios[id_usuario] = usuario
        self.ids_usuarios.add(id_usuario)

        print(" Usuario registrado")

    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado")
        else:
            print("Usuario no encontrado")

    # =====================
    # PRÉSTAMOS
    # =====================

    def prestar_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return

        if isbn not in self.catalogo:
            print("Libro no existe")
            return

        libro = self.catalogo[isbn]

        if not libro.esta_disponible():
            print("Libro no disponible")
            return

        usuario = self.usuarios[id_usuario]

        libro.prestar()
        usuario.agregar_prestamo(libro)

        print("📚 Préstamo realizado")

    def devolver_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return

        usuario = self.usuarios[id_usuario]

        libro = usuario.devolver_libro(isbn)

        if libro:
            libro.devolver()
            print("Libro devuelto correctamente")
        else:
            print("El usuario no tiene ese libro")

    # =====================
    # BÚSQUEDAS
    # =====================

    def buscar_por_titulo(self, titulo):

        for libro in self.catalogo.values():
            if titulo.lower() in libro.obtener_titulo().lower():
                print(libro)

    def buscar_por_autor(self, autor):

        for libro in self.catalogo.values():
            if autor.lower() in libro.obtener_autor().lower():
                print(libro)

    def buscar_por_categoria(self, categoria):

        for libro in self.catalogo.values():
            if categoria.lower() in libro.obtener_categoria().lower():
                print(libro)

    # =====================
    # LISTAR PRÉSTAMOS
    # =====================

    def libros_usuario(self, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no existe")
            return

        usuario = self.usuarios[id_usuario]

        libros = usuario.obtener_libros()

        if not libros:
            print("No tiene libros prestados")
            return

        for libro in libros:

            print(libro)

