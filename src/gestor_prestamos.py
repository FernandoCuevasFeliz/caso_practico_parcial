class GestorPrestamos:
    def __init__(self):
        self.prestamos = []

    def realizar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def realizar_devolucion(self, id_prestamo):
        for prestamo in self.prestamos:
            if prestamo.get_id_prestamo() == id_prestamo:
                prestamo.set_fecha_devolucion("2024-07-05")  # O la fecha actual
                self.prestamos.remove(prestamo)
                break

    def buscar_prestamos(self):
        return self.prestamos
