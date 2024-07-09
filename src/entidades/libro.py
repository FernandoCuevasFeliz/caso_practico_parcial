class Libro:
    def __init__(self, id_libro, titulo, autor, isbn, cantidad_disponible):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.cantidad_disponible = cantidad_disponible

    # Getters y setters
    def get_id_libro(self):
        return self.id_libro

    def set_id_libro(self, id_libro):
        self.id_libro = id_libro

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_cantidad_disponible(self):
        return self.cantidad_disponible

    def set_cantidad_disponible(self, cantidad_disponible):
        self.cantidad_disponible = cantidad_disponible