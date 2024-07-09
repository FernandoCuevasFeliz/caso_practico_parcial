from locust import HttpUser, task, between

class BibliotecaUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def view_books(self):
        self.client.get("/libros")

    @task
    def view_users(self):
        self.client.get("/usuarios")

    @task
    def borrow_book(self):
        self.client.post("/prestamos", json={"idUsuario": 1, "idLibro": 1, "fechaPrestamo": "2024-07-01", "fechaDevolucion": "2024-07-15"})
