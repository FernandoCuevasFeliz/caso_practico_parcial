from gestor_libros import GestorLibros
from gestor_usuarios import GestorUsuarios
from gestor_prestamos import GestorPrestamos
from generador_reportes import GeneradorReportes
from libro import Libro
from usuario import Usuario
from prestamo import Prestamo

def main():
    # Inicialización de los gestores
    gestor_libros = GestorLibros()
    gestor_usuarios = GestorUsuarios()
    gestor_prestamos = GestorPrestamos()
    generador_reportes = GeneradorReportes(gestor_prestamos)
    
    # Registrar algunos libros y usuarios para probar
    libro1 = Libro(1, "Cien Años de Soledad", "Gabriel García Márquez", "1234567890", 10)
    libro2 = Libro(2, "El Quijote", "Miguel de Cervantes", "0987654321", 5)
    usuario1 = Usuario(1, "Juan Pérez", "Calle Falsa 123", "555-1234")
    usuario2 = Usuario(2, "María López", "Avenida Siempre Viva 742", "555-5678")
    
    gestor_libros.registrar_libro(libro1)
    gestor_libros.registrar_libro(libro2)
    gestor_usuarios.registrar_usuario(usuario1)
    gestor_usuarios.registrar_usuario(usuario2)
    
    # Realizar un préstamo
    prestamo1 = Prestamo(1, usuario1.get_id_usuario(), libro1.get_id_libro(), "2024-07-01", "2024-07-15")
    gestor_prestamos.realizar_prestamo(prestamo1)
    
    # Devolver el libro
    gestor_prestamos.realizar_devolucion(prestamo1.get_id_prestamo())
    
    # Generar reportes
    generador_reportes.generar_reporte_libros_prestados()
    generador_reportes.generar_reporte_libros_devueltos()
    generador_reportes.generar_estadisticas_uso()
    
    print("Operaciones de prueba completadas.")

if __name__ == "__main__":
    main()
