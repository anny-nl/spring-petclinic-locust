mkdir -p results
echo "Rodando CENÁRIO MODERADO (100 usuários por 10 minutos)..."

locust -f locustfile.py \
  --host http://localhost:8080 \
  --headless \
  -u 100 -r 10 -t 10m \
  --csv=results/cenario_medio \
  --csv-full-history

echo "Resultados salvos em results/cenario_medio_*.csv"

