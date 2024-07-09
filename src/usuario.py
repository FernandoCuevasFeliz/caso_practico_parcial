class Usuario:
    def __init__(self, id_usuario, nombre, direccion, contacto):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.direccion = direccion
        self.contacto = contacto

    # Getters y setters
    def get_id_usuario(self):
        return self.id_usuario

    def set_id_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_contacto(self):
        return self.contacto

    def set_contacto(self, contacto):
        self.contacto = contacto