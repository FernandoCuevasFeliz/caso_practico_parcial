import unittest
from src.gestor_libros import GestorLibros
from src.gestor_usuarios import GestorUsuarios
from src.gestor_prestamos import GestorPrestamos
from src.generador_reportes import GeneradorReportes
from src.libro import Libro
from src.usuario import Usuario
from src.prestamo import Prestamo

class TestIntegracionBiblioteca(unittest.TestCase):

    def setUp(self):
        # Inicializar los gestores
        self.gestor_libros = GestorLibros()
        self.gestor_usuarios = GestorUsuarios()
        self.gestor_prestamos = GestorPrestamos()
        self.generador_reportes = GeneradorReportes(self.gestor_prestamos)

        # Crear datos de prueba
        self.libro1 = Libro(1, "Cien Años de Soledad", "Gabriel García Márquez", "1234567890", 10)
        self.libro2 = Libro(2, "El Quijote", "Miguel de Cervantes", "0987654321", 5)
        self.usuario1 = Usuario(1, "Juan Pérez", "Calle Falsa 123", "555-1234")
        self.usuario2 = Usuario(2, "María López", "Avenida Siempre Viva 742", "555-5678")

    def test_registro_libros_y_usuarios(self):
        # Registrar libros
        self.gestor_libros.registrar_libro(self.libro1)
        self.gestor_libros.registrar_libro(self.libro2)

        # Registrar usuarios
        self.gestor_usuarios.registrar_usuario(self.usuario1)
        self.gestor_usuarios.registrar_usuario(self.usuario2)

        # Verificar registros
        self.assertEqual(len(self.gestor_libros.libros), 2)
        self.assertEqual(len(self.gestor_usuarios.usuarios), 2)

    def test_prestamo_y_devolucion(self):
        # Registrar libros y usuarios
        self.gestor_libros.registrar_libro(self.libro1)
        self.gestor_libros.registrar_libro(self.libro2)
        self.gestor_usuarios.registrar_usuario(self.usuario1)
        self.gestor_usuarios.registrar_usuario(self.usuario2)

        # Realizar préstamos
        prestamo1 = Prestamo(1, self.usuario1.get_id_usuario(), self.libro1.get_id_libro(), "2024-07-01", None)
        prestamo2 = Prestamo(2, self.usuario2.get_id_usuario(), self.libro2.get_id_libro(), "2024-07-02", None)
        self.gestor_prestamos.realizar_prestamo(prestamo1)
        self.gestor_prestamos.realizar_prestamo(prestamo2)

        # Verificar préstamos
        self.assertEqual(len(self.gestor_prestamos.prestamos), 2)

        # Realizar devolución de un libro
        self.gestor_prestamos.realizar_devolucion(prestamo1.get_id_prestamo())

        # Verificar devolución
        self.assertEqual(len(self.gestor_prestamos.prestamos), 1)

    def test_generacion_reportes(self):
        # Registrar libros y usuarios
        self.gestor_libros.registrar_libro(self.libro1)
        self.gestor_libros.registrar_libro(self.libro2)
        self.gestor_usuarios.registrar_usuario(self.usuario1)
        self.gestor_usuarios.registrar_usuario(self.usuario2)

        # Realizar préstamos
        prestamo1 = Prestamo(1, self.usuario1.get_id_usuario(), self.libro1.get_id_libro(), "2024-07-01", None)
        prestamo2 = Prestamo(2, self.usuario2.get_id_usuario(), self.libro2.get_id_libro(), "2024-07-02", None)
        self.gestor_prestamos.realizar_prestamo(prestamo1)
        self.gestor_prestamos.realizar_prestamo(prestamo2)

        # Generar reporte de libros prestados
        reporte_prestados = self.generador_reportes.generar_reporte_libros_prestados()
        self.assertEqual(len(reporte_prestados), 2)

        # Realizar devolución de un libro
        self.gestor_prestamos.realizar_devolucion(prestamo1.get_id_prestamo())

        # Generar reporte de libros prestados nuevamente
        reporte_prestados = self.generador_reportes.generar_reporte_libros_prestados()
        self.assertEqual(len(reporte_prestados), 1)

if __name__ == '__main__':
    unittest.main()
