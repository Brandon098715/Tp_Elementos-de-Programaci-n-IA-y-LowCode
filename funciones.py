import json
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt


ARCHIVO_DATOS = "datos.json"


def cargar_gastos() -> list:
    """Lee los gastos guardados en datos.json."""
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            gastos = json.load(archivo)
            return gastos
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def guardar_gastos(gastos: list) -> None:
    """Guarda la lista de gastos en datos.json."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(gastos, archivo, indent=4, ensure_ascii=False)


def validar_fecha(fecha: str) -> bool:
    """Devuelve True si la fecha tiene formato AAAA-MM-DD."""
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def agregar_gasto(
    gastos: list,
    fecha: str,
    categoria: str,
    descripcion: str,
    monto: float,
) -> dict:
    """Crea un gasto nuevo y lo agrega a la lista."""
    nuevo_id = 1

    for gasto in gastos:
        if gasto["id"] >= nuevo_id:
            nuevo_id = gasto["id"] + 1

    nuevo_gasto = {
        "id": nuevo_id,
        "fecha": fecha,
        "categoria": categoria,
        "descripcion": descripcion,
        "monto": monto,
    }

    gastos.append(nuevo_gasto)
    return nuevo_gasto


def modificar_gasto(
    gastos: list,
    id_gasto: int,
    fecha: str,
    categoria: str,
    descripcion: str,
    monto: float,
) -> bool:
    """Busca un gasto por ID y modifica sus datos."""
    for gasto in gastos:
        if gasto["id"] == id_gasto:
            gasto["fecha"] = fecha
            gasto["categoria"] = categoria
            gasto["descripcion"] = descripcion
            gasto["monto"] = monto
            return True

    return False


def eliminar_gasto(gastos: list, id_gasto: int) -> bool:
    """Busca un gasto por ID y lo elimina."""
    for gasto in gastos:
        if gasto["id"] == id_gasto:
            gastos.remove(gasto)
            return True

    return False


def filtrar_por_categoria(gastos: list, categoria: str) -> list:
    """Devuelve solamente los gastos de una categoría."""
    resultado = []

    for gasto in gastos:
        if gasto["categoria"] == categoria:
            resultado.append(gasto)

    return resultado


def calcular_indicadores(gastos: list) -> tuple:
    """Calcula total gastado, promedio y gasto mayor."""
    if len(gastos) == 0:
        return 0, 0, 0

    total = 0
    mayor = 0

    for gasto in gastos:
        total = total + gasto["monto"]

        if gasto["monto"] > mayor:
            mayor = gasto["monto"]

    promedio = total / len(gastos)

    return total, promedio, mayor


def crear_grafico(gastos: list) -> None:
    """Crea un gráfico de barras con el total por categoría."""
    datos = pd.DataFrame(gastos)
    totales = datos.groupby("categoria")["monto"].sum()

    totales.plot(kind="bar")

    plt.title("Gastos por categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Monto")
    plt.tight_layout()

    plt.savefig("grafico.png")
    plt.show()
