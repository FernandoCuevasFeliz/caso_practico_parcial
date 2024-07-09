from gestor_libros import GestorLibros
from gestor_usuarios import GestorUsuarios
from gestor_prestamos import GestorPrestamos
from generador_reportes import GeneradorReportes
from libro import Libro
from usuario import Usuario
from prestamo import Prestamo

def mostrar_libros(gestor_libros):
    print("\nLibros Registrados:")
    for libro in gestor_libros.libros:
        print(f"ID: {libro.get_id_libro()}, Título: {libro.get_titulo()}, Autor: {libro.get_autor()}, ISBN: {libro.get_isbn()}, Cantidad Disponible: {libro.get_cantidad_disponible()}")

def mostrar_usuarios(gestor_usuarios):
    print("\nUsuarios Registrados:")
    for usuario in gestor_usuarios.usuarios:
        print(f"ID: {usuario.get_id_usuario()}, Nombre: {usuario.get_nombre()}, Dirección: {usuario.get_direccion()}, Contacto: {usuario.get_contacto()}")

def mostrar_prestamos(gestor_prestamos):
    print("\nPréstamos Registrados:")
    for prestamo in gestor_prestamos.prestamos:
        print(f"ID Préstamo: {prestamo.get_id_prestamo()}, ID Usuario: {prestamo.get_id_usuario()}, ID Libro: {prestamo.get_id_libro()}, Fecha Préstamo: {prestamo.get_fecha_prestamo()}, Fecha Devolución: {prestamo.get_fecha_devolucion()}")

def mostrar_libros_devueltos_y_pendientes(gestor_libros, gestor_prestamos):
    devueltos = []
    pendientes = []

    for libro in gestor_libros.libros:
        libro_prestado = any(prestamo.get_id_libro() == libro.get_id_libro() for prestamo in gestor_prestamos.prestamos)
        if libro_prestado:
            pendientes.append(libro)
        else:
            devueltos.append(libro)

    print("\nLibros Devueltos:")
    for libro in devueltos:
        print(f"ID: {libro.get_id_libro()}, Título: {libro.get_titulo()}")

    print("\nLibros Pendientes de Devolución:")
    for libro in pendientes:
        print(f"ID: {libro.get_id_libro()}, Título: {libro.get_titulo()}")

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
    
    # Mostrar libros y usuarios registrados
    mostrar_libros(gestor_libros)
    mostrar_usuarios(gestor_usuarios)
    
    # Realizar dos préstamos
    prestamo1 = Prestamo(1, usuario1.get_id_usuario(), libro1.get_id_libro(), "2024-07-01", "2024-07-15")
    prestamo2 = Prestamo(2, usuario2.get_id_usuario(), libro2.get_id_libro(), "2024-07-02", "2024-07-16")
    gestor_prestamos.realizar_prestamo(prestamo1)
    gestor_prestamos.realizar_prestamo(prestamo2)
    
    # Mostrar préstamos registrados
    mostrar_prestamos(gestor_prestamos)
    
    # Devolver uno de los libros
    gestor_prestamos.realizar_devolucion(prestamo1.get_id_prestamo())
    
    # Mostrar préstamos después de la devolución
    mostrar_prestamos(gestor_prestamos)
    
    # Mostrar libros devueltos y pendientes de devolución
    mostrar_libros_devueltos_y_pendientes(gestor_libros, gestor_prestamos)
    
    # Generar reportes (pendiente de implementación)
    generador_reportes.generar_reporte_libros_prestados()
    generador_reportes.generar_reporte_libros_devueltos()
    generador_reportes.generar_estadisticas_uso()
    
    print("\nOperaciones de prueba completadas.")

if __name__ == "__main__":
    main()
