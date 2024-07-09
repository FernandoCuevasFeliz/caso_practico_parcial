import unittest
from src.gestor_prestamos import GestorPrestamos
from src.prestamo import Prestamo
from src.libro import Libro
from src.usuario import Usuario

class TestGestorPrestamos(unittest.TestCase):
    def setUp(self):
        self.gestor_prestamos = GestorPrestamos()
        self.libro = Libro(1, "Libro 1", "Autor 1", "123456789", 5)
        self.usuario = Usuario(1, "Usuario 1", "Dirección 1", "Contacto 1")
        self.prestamo = Prestamo(1, self.usuario.get_id_usuario(), self.libro.get_id_libro(), "2024-07-01", "2024-07-15")

    def test_realizar_prestamo(self):
        self.gestor_prestamos.realizar_prestamo(self.prestamo)
        self.assertEqual(len(self.gestor_prestamos.prestamos), 1)
        self.assertEqual(self.gestor_prestamos.prestamos[0].get_id_prestamo(), 1)

    def test_realizar_devolucion(self):
        self.gestor_prestamos.realizar_prestamo(self.prestamo)
        self.gestor_prestamos.realizar_devolucion(1)
        self.assertEqual(len(self.gestor_prestamos.prestamos), 0)

if __name__ == '__main__':
    unittest.main()
