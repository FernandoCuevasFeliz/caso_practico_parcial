from src.usuario import Usuario

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def actualizar_usuario(self, id_usuario, nuevo_usuario):
        for idx, usuario in enumerate(self.usuarios):
            if usuario.get_id_usuario() == id_usuario:
                self.usuarios[idx] = nuevo_usuario
                break

    def eliminar_usuario(self, id_usuario):
        self.usuarios = [usuario for usuario in self.usuarios if usuario.get_id_usuario() != id_usuario]

    def buscar_usuarios(self):
        return [usuario.get_nombre() for usuario in self.usuarios]
