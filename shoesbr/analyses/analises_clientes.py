import os
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from dotenv import load_dotenv

# carrega variáveis do .env
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# conexão segura
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

query = """
select
    customer_name,
    total_gasto
from marts.dim_clientes
order by total_gasto desc
limit 10
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(14, 7))

# gráfico de barras
bars = plt.bar(
    df["customer_name"],
    df["total_gasto"]
)

# título principal
plt.title(
    "Top 10 Clientes por Total Gasto",
    fontsize=18,
    fontweight='bold',
    pad=20
)

# labels dos eixos
plt.xlabel(
    "Clientes",
    fontsize=12,
    labelpad=10
)

plt.ylabel(
    "Total Gasto (R$)",
    fontsize=12,
    labelpad=10
)

# rotação dos nomes
plt.xticks(
    rotation=45,
    ha="right",
    fontsize=10
)

# tamanho eixo y
plt.yticks(fontsize=10)

# grid horizontal
plt.grid(
    axis='y',
    linestyle='--',
    alpha=0.4
)

# adiciona valor acima das barras
for bar in bars:
    
    altura = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        altura,
        f'R$ {altura:,.2f}',
        ha='center',
        va='bottom',
        fontsize=9
    )

# remove bordas superiores/direitas
ax = plt.gca()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ajusta layout
plt.tight_layout()

# salva gráfico
plt.savefig(
    "docs/images/top_clientes_total_gasto.png",
    dpi=300,
    bbox_inches='tight'
)

plt.savefig("docs/images/top_clientes_total_gasto.png")