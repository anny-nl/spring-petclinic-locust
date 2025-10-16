mkdir -p results
echo "Rodando CENÁRIO DE PICO (200 usuários por 5 minutos)..."

locust -f locustfile.py \
  --host http://localhost:8080 \
  --headless \
  -u 200 -r 20 -t 5m \
  --csv=results/cenario_pico \
  --csv-full-history

echo "Resultados salvos em results/cenario_pico_*.csv"

