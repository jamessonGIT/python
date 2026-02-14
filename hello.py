import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# 1) Ler o arquivo já limpo
df = pd.read_csv("nasa.csv")  # <-- coloque o nome do seu arquivo

# 2) Trocar -999 por NA
df = df.replace(-999, pd.NA).replace(-999.0, pd.NA)

# 3) YEAR + DOY → data
def doy_to_date(year, doy):
    return (datetime(int(year), 1, 1) + timedelta(days=int(doy)-1)).date()

df["date"] = [doy_to_date(y, d) for y, d in zip(df["YEAR"], df["DOY"])]

# 4) Reordenar colunas
df = df[["date"] + [c for c in df.columns if c != "date"]]

# 5) Salvar base limpa
df.to_csv("nasa_power_clean.csv", index=False)

# 6) Resumo mensal
monthly = (
    df.set_index("date")
      .groupby(pd.Grouper(freq="MS"))
      [["PRECTOTCORR", "RH2M", "QV2M", "IMERG_PRECTOT"]]
      .mean(numeric_only=True)
      .reset_index()
)

monthly.to_csv("nasa_power_monthly_summary.csv", index=False)

# 7) Gráfico de exemplo
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["PRECTOTCORR"], label="Precipitação (mm/dia)")
plt.xlabel("Data")
plt.ylabel("Precipitação (mm/dia)")
plt.title("NASA/POWER — Série de precipitação diária")
plt.legend()
plt.tight_layout()
plt.savefig("nasa_power_plot.png", dpi=150)
plt.close()

print("Processamento concluído!")