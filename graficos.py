"""Funciones relacionadas con el análisis y los gráficos."""

import pandas as pd
import matplotlib.pyplot as plt


def crear_grafico(gastos: list) -> None:
    """Muestra y guarda un gráfico con el total gastado por categoría."""

    # pandas transforma la lista de diccionarios en una tabla.
    datos = pd.DataFrame(gastos)

    # Agrupamos las filas por categoría y sumamos sus montos.
    totales = datos.groupby("categoria")["monto"].sum()

    # Matplotlib dibuja el gráfico de barras.
    totales.plot(kind="bar")
    plt.title("Gastos por categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Monto")
    plt.tight_layout()

    # También guardamos el gráfico como archivo para la entrega.
    plt.savefig("grafico.png")
    plt.show()
    plt.close()
