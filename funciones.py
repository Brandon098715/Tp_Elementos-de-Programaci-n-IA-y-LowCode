"""Funciones con la lógica principal de la aplicación."""

from datetime import datetime


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

    # Buscamos el ID más alto para crear uno nuevo sin repetirlo.
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
