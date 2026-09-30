"""Funciones encargadas de leer y guardar los datos del programa."""

import json

ARCHIVO_DATOS = "datos.json"


def cargar_gastos() -> list:
    """Lee los gastos guardados en datos.json.

    Si el archivo no existe o está dañado, devuelve una lista vacía
    para que la aplicación pueda seguir funcionando.
    """
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def guardar_gastos(gastos: list) -> None:
    """Guarda la lista de gastos en datos.json."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(gastos, archivo, indent=4, ensure_ascii=False)
