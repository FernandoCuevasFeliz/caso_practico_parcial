from src.prestamo import Prestamo

class GestorPrestamos:
    def __init__(self):
        self.prestamos = []

    def realizar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def realizar_devolucion(self, id_prestamo):
        for prestamo in self.prestamos:
            if prestamo.get_id_prestamo() == id_prestamo:
                self.prestamos.remove(prestamo)
                break

    def buscar_prestamos(self):
        return [prestamo.get_id_prestamo() for prestamo in self.prestamos]
