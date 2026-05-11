# ================================
# 📊 Top 5 Receita Líquida por Produto e Método de Pagamento
# ================================

import os
import pandas as pd
import matplotlib.pyplot as plt

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

query = """
SELECT
    name_product,
    payment_method,
    SUM(receita_liquida) AS receita_liquida
FROM marts.fct_vendas
GROUP BY
    name_product,
    payment_method
ORDER BY receita_liquida DESC
LIMIT 5
"""

df = pd.read_sql(query, engine)

os.makedirs("assets/charts", exist_ok=True)

df["label"] = df["name_product"] + " | " + df["payment_method"]

plt.figure(figsize=(14, 7))

bars = plt.barh(
    df["label"],
    df["receita_liquida"]
)

plt.title(
    "Top 5 Receita Líquida por Produto e Método de Pagamento",
    fontsize=18,
    fontweight="bold",
    pad=20
)

plt.xlabel(
    "Receita Líquida (R$)",
    fontsize=12,
    labelpad=10
)

plt.ylabel(
    "Produto | Método de Pagamento",
    fontsize=12,
    labelpad=10
)

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.4
)

plt.gca().invert_yaxis()

for bar in bars:
    largura = bar.get_width()

    plt.text(
        largura,
        bar.get_y() + bar.get_height() / 2,
        f" R$ {largura:,.2f}",
        va="center",
        fontsize=10,
        fontweight="bold"
    )

ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()

plt.savefig(
    "docs/images/top5_receita_liquida_produto_pagamento.png",
    dpi=300,
    bbox_inches="tight"
)

