# Avaliação de Desempenho – Spring PetClinic (Microservices) com Locust

## Objetivo
Medir e analisar o desempenho do sistema **Spring PetClinic – Microservices** utilizando a ferramenta **Locust**.

## Tecnologias
- Docker & Docker Compose
- Python 3 + Locust
- Spring PetClinic (versão microservices)

---

## Como executar

### 1. Clonar o projeto
```bash
git clone https://github.com/spring-petclinic/spring-petclinic-microservices.git
cd spring-petclinic-microservices

# Subir a aplicação:
 docker compose up --build -d

# A aplicação deve responder em:
http://localhost:8080/owners

# Executar os testes
bash run_leve.sh
bash run_medio.sh
bash run_pico.sh
\\ Os resultados serão salvos na pasta results/.

#Gerar resumo final:
python analisar_csvs.py




