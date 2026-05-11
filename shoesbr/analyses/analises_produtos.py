# ================================
# 📊 Analytics - Produtos
# ================================

import os
import pandas as pd
import matplotlib.pyplot as plt

from sqlalchemy import create_engine
from dotenv import load_dotenv

# ================================
# carregar variáveis ambiente
# ================================

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# ================================
# conexão postgres
# ================================

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ================================
# query analytics
# ================================

query = """
SELECT
    name_product,
    total_faturado,
    total_vendido,
    total_estornado
FROM marts.dim_produtos
ORDER BY total_faturado DESC
LIMIT 10
"""

# dataframe
df = pd.read_sql(query, engine)

# ================================
# cria pasta automaticamente
# ================================

os.makedirs("assets/charts", exist_ok=True)

# ================================
# gráfico
# ================================

plt.figure(figsize=(15,8))

bars = plt.bar(
    df["name_product"],
    df["total_faturado"]
)

# título
plt.title(
    "Top 10 Produtos por Total Faturado",
    fontsize=20,
    fontweight='bold',
    pad=20
)

# eixos
plt.xlabel(
    "Produtos",
    fontsize=13,
    labelpad=15
)

plt.ylabel(
    "Total Faturado (R$)",
    fontsize=13,
    labelpad=15
)

# labels eixo x
plt.xticks(
    rotation=45,
    ha='right',
    fontsize=10
)

# labels eixo y
plt.yticks(fontsize=10)

# grid horizontal
plt.grid(
    axis='y',
    linestyle='--',
    alpha=0.4
)

# valores nas barras
for bar in bars:

    valor = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        valor,
        f'R$ {valor:,.2f}',
        ha='center',
        va='bottom',
        fontsize=9,
        fontweight='bold'
    )

# remove bordas desnecessárias
ax = plt.gca()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# layout
plt.tight_layout()

# salva gráfico
plt.savefig(
    "docs/images/top_produtos_faturamento.png",
    dpi=300,
    bbox_inches='tight'
)


