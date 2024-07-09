import unittest
from src.gestor_libros import GestorLibros
from src.libro import Libro

class TestGestorLibros(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorLibros()
        self.libro1 = Libro(1, "Libro 1", "Autor 1", "123456789", 5)
        self.libro2 = Libro(2, "Libro 2", "Autor 2", "987654321", 3)

    def test_registrar_libro(self):
        self.gestor.registrar_libro(self.libro1)
        self.assertEqual(len(self.gestor.libros), 1)
        self.assertEqual(self.gestor.libros[0].get_titulo(), "Libro 1")

    def test_actualizar_libro(self):
        self.gestor.registrar_libro(self.libro1)
        libro_actualizado = Libro(1, "Libro 1 Actualizado", "Autor 1", "123456789", 5)
        self.gestor.actualizar_libro(1, libro_actualizado)
        self.assertEqual(self.gestor.libros[0].get_titulo(), "Libro 1 Actualizado")

    def test_eliminar_libro(self):
        self.gestor.registrar_libro(self.libro1)
        self.gestor.eliminar_libro(1)
        self.assertEqual(len(self.gestor.libros), 0)

if __name__ == '__main__':
    unittest.main()
