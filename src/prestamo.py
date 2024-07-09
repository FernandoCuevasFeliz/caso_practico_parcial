class Prestamo:
    def __init__(self, id_prestamo, id_usuario, id_libro, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    # Getters y setters
    def get_id_prestamo(self):
        return self.id_prestamo

    def set_id_prestamo(self, id_prestamo):
        self.id_prestamo = id_prestamo

    def get_id_usuario(self):
        return self.id_usuario

    def set_id_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    def get_id_libro(self):
        return self.id_libro

    def set_id_libro(self, id_libro):
        self.id_libro = id_libro

    def get_fecha_prestamo(self):
        return self.fecha_prestamo

    def set_fecha_prestamo(self, fecha_prestamo):
        self.fecha_prestamo = fecha_prestamo

    def get_fecha_devolucion(self):
        return self.fecha_devolucion

    def set_fecha_devolucion(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion