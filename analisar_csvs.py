import pandas as pd
import glob
import os

def resumo_csv(prefixo, warmup_segundos=60):
    arquivos = glob.glob(f"results/{prefixo}*_stats.csv")
    if not arquivos:
        print(f"Nenhum arquivo encontrado para {prefixo}")
        return None

    dfs = []
    for arq in arquivos:
        df = pd.read_csv(arq)
        if "Average Response Time" in df.columns:
            df["cenario"] = prefixo
            dfs.append(df)
    if not dfs:
        return None

    dados = pd.concat(dfs)
    resumo = dados.groupby("cenario").agg({
        "Average Response Time": "mean",
        "Max Response Time": "max",
        "Requests/s": "mean",
        "Total Request Count": "sum",
        "Failure Count": "sum",
        "Success %": "mean"
    }).reset_index()

    return resumo

cenarios = ["cenario_leve", "cenario_medio", "cenario_pico"]
todos = [resumo_csv(c) for c in cenarios if resumo_csv(c) is not None]
resultado = pd.concat(todos)
print(resultado)
resultado.to_csv("results/resumo_final.csv", index=False)
print("\nResumo salvo em results/resumo_final.csv")

