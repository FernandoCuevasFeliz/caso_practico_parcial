class GeneradorReportes:
    def __init__(self, gestor_prestamos):
        self.gestor_prestamos = gestor_prestamos

    def generar_reporte_libros_prestados(self):
        reporte = []
        for prestamo in self.gestor_prestamos.buscar_prestamos():
            if prestamo.get_fecha_devolucion() is None:
                reporte.append({
                    "id_prestamo": prestamo.get_id_prestamo(),
                    "id_libro": prestamo.get_id_libro(),
                    "id_usuario": prestamo.get_id_usuario(),
                    "fecha_prestamo": prestamo.get_fecha_prestamo()
                })
        return reporte

    def generar_reporte_libros_devueltos(self):
        reporte = []
        for prestamo in self.gestor_prestamos.buscar_prestamos():
            if prestamo.get_fecha_devolucion() is None:
                reporte.append({
                    "id_prestamo": prestamo.get_id_prestamo(),
                    "id_libro": prestamo.get_id_libro(),
                    "id_usuario": prestamo.get_id_usuario(),
                    "fecha_prestamo": prestamo.get_fecha_prestamo()
                })
        return reporte

    def generar_estadisticas_uso(self):
        estadisticas = {
            "libros_mas_prestados": {},
            "usuarios_mas_activos": {}
        }

        for prestamo in self.gestor_prestamos.buscar_prestamos():
            libro_id = prestamo.get_id_libro()
            usuario_id = prestamo.get_id_usuario()

            if libro_id not in estadisticas["libros_mas_prestados"]:
                estadisticas["libros_mas_prestados"][libro_id] = 0
            estadisticas["libros_mas_prestados"][libro_id] += 1

            if usuario_id not in estadisticas["usuarios_mas_activos"]:
                estadisticas["usuarios_mas_activos"][usuario_id] = 0
            estadisticas["usuarios_mas_activos"][usuario_id] += 1

        libros_mas_prestados = sorted(
            estadisticas["libros_mas_prestados"].items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        usuarios_mas_activos = sorted(
            estadisticas["usuarios_mas_activos"].items(), 
            key=lambda x: x[1], 
            reverse=True
        )

        return {
            "libros_mas_prestados": libros_mas_prestados,
            "usuarios_mas_activos": usuarios_mas_activos
        }
