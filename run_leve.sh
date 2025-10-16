#!/usr/bin/env bash
mkdir -p results
echo "Rodando CENÁRIO LEVE (50 usuários por 10 minutos)..."

locust -f locustfile.py \
  --host http://localhost:8080 \
  --headless \
  -u 50 -r 10 -t 10m \
  --csv=results/cenario_leve \
  --csv-full-history

echo "Resultados salvos em results/cenario_leve_*.csv"

