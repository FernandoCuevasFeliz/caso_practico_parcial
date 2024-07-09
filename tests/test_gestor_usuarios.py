import unittest
from src.gestor_usuarios import GestorUsuarios
from src.usuario import Usuario

class TestGestorUsuarios(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorUsuarios()
        self.usuario1 = Usuario(1, "Usuario 1", "Dirección 1", "Contacto 1")
        self.usuario2 = Usuario(2, "Usuario 2", "Dirección 2", "Contacto 2")

    def test_registrar_usuario(self):
        self.gestor.registrar_usuario(self.usuario1)
        self.assertEqual(len(self.gestor.usuarios), 1)
        self.assertEqual(self.gestor.usuarios[0].get_nombre(), "Usuario 1")

    def test_actualizar_usuario(self):
        self.gestor.registrar_usuario(self.usuario1)
        usuario_actualizado = Usuario(1, "Usuario 1 Actualizado", "Dirección 1", "Contacto 1")
        self.gestor.actualizar_usuario(1, usuario_actualizado)
        self.assertEqual(self.gestor.usuarios[0].get_nombre(), "Usuario 1 Actualizado")

    def test_eliminar_usuario(self):
        self.gestor.registrar_usuario(self.usuario1)
        self.gestor.eliminar_usuario(1)
        self.assertEqual(len(self.gestor.usuarios), 0)

if __name__ == '__main__':
    unittest.main()
