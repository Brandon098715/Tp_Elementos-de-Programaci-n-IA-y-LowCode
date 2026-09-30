"""Pruebas simples de las funciones principales del programa."""

from funciones import (
    agregar_gasto,
    calcular_indicadores,
    eliminar_gasto,
    filtrar_por_categoria,
    modificar_gasto,
    validar_fecha,
)


def mostrar_resultado(nombre: str, resultado: bool) -> None:
    """Muestra OK o ERROR para cada prueba."""

    if resultado:
        print("OK   -", nombre)
    else:
        print("ERROR-", nombre)


# Usamos una lista vacía para probar sin modificar datos.json.
gastos_prueba = []

agregar_gasto(
    gastos_prueba,
    "2026-09-30",
    "Comida",
    "Almuerzo",
    10000,
)

mostrar_resultado(
    "Agregar gasto",
    len(gastos_prueba) == 1,
)

modificar_gasto(
    gastos_prueba,
    1,
    "2026-09-30",
    "Comida",
    "Cena",
    12000,
)

mostrar_resultado(
    "Modificar gasto",
    gastos_prueba[0]["descripcion"] == "Cena"
    and gastos_prueba[0]["monto"] == 12000,
)

agregar_gasto(
    gastos_prueba,
    "2026-09-30",
    "Transporte",
    "Colectivo",
    3000,
)

filtrados = filtrar_por_categoria(
    gastos_prueba,
    "Comida",
)

mostrar_resultado(
    "Filtrar por categoría",
    len(filtrados) == 1
    and filtrados[0]["categoria"] == "Comida",
)

total, promedio, mayor = calcular_indicadores(gastos_prueba)

mostrar_resultado(
    "Calcular indicadores",
    total == 15000
    and promedio == 7500
    and mayor == 12000,
)

mostrar_resultado(
    "Validar fecha correcta",
    validar_fecha("2026-09-30"),
)

mostrar_resultado(
    "Detectar fecha incorrecta",
    not validar_fecha("30/09/2026"),
)

eliminar_gasto(gastos_prueba, 1)

mostrar_resultado(
    "Eliminar gasto",
    len(gastos_prueba) == 1
    and gastos_prueba[0]["id"] == 2,
)

print()
print("Pruebas finalizadas.")
