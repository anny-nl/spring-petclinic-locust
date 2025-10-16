from locust import HttpUser, between, task
import random

class PetClinicUser(HttpUser):
    # tempo de espera entre as requisições (simula comportamento humano)
    wait_time = between(1, 3)

    @task(40)
    def listar_donos(self):
        self.client.get("/owners")

    @task(30)
    def detalhes_dono(self):
        owner_id = random.randint(1, 20)  # IDs já cadastrados
        self.client.get(f"/owners/{owner_id}")

    @task(20)
    def listar_vets(self):
        self.client.get("/vets")

    @task(10)
    def criar_dono(self):
        novo_dono = {
            "firstName": f"User{random.randi
