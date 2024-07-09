class GestorLibros:
    def __init__(self):
        self.libros = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def actualizar_libro(self, id_libro, nuevo_libro):
        for idx, libro in enumerate(self.libros):
            if libro.get_id_libro() == id_libro:
                self.libros[idx] = nuevo_libro
                break

    def eliminar_libro(self, id_libro):
        self.libros = [libro for libro in self.libros if libro.get_id_libro() != id_libro]

    def buscar_libros(self):
        return [libro.get_titulo() for libro in self.libros]
