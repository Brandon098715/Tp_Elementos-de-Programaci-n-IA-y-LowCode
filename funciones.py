import json
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt

ARCHIVO_DATOS: str = "datos.json"
ARCHIVO_GRAFICO: str = "grafico.png"
CATEGORIAS: list[str] = ["Comida", "Transporte", "Servicios", "Ocio", "Salud", "Otros"]


# ---------- Persistencia ----------

def cargar_gastos(ruta: str = ARCHIVO_DATOS) -> list[dict]:
    """Lee los gastos del archivo JSON. Si no existe o está dañado, devuelve una lista vacía."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            gastos: list[dict] = json.load(archivo)
    except FileNotFoundError:
        print(f"Aviso: no se encontró '{ruta}'. Se empieza con una lista vacía.")
        gastos = []
    except json.JSONDecodeError:
        print(f"Aviso: '{ruta}' está dañado. Se empieza con una lista vacía.")
        gastos = []
    return gastos


def guardar_gastos(gastos: list[dict], ruta: str = ARCHIVO_DATOS) -> None:
    """Guarda la lista de gastos en el archivo JSON."""
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(gastos, archivo, ensure_ascii=False, indent=4)


# ---------- Validación y entrada de datos ----------

def pedir_monto() -> float:
    """Pide un monto hasta que sea un número mayor a 0."""
    while True:
        texto: str = input("Monto: ").strip()
        try:
            monto: float = float(texto)
        except ValueError:
            print("Error: el monto debe ser un número (ej: 1500 o 1500.50).")
            continue
        if monto <= 0:
            print("Error: el monto debe ser mayor a 0.")
            continue
        return monto


def pedir_fecha() -> str:
    """Pide una fecha AAAA-MM-DD válida. Si se presiona Enter, devuelve la fecha de hoy."""
    while True:
        texto: str = input("Fecha (AAAA-MM-DD, Enter = hoy): ").strip()
        if texto == "":
            return datetime.now().strftime("%Y-%m-%d")
        try:
            fecha: datetime = datetime.strptime(texto, "%Y-%m-%d")
        except ValueError:
            print("Error: fecha inválida. Usá el formato AAAA-MM-DD (ej: 2026-09-20).")
            continue
        return fecha.strftime("%Y-%m-%d")


def pedir_categoria() -> str:
    """Muestra las categorías numeradas y pide elegir una."""
    print("Categorías:")
    numero: int = 1
    for categoria in CATEGORIAS:
        print(f"  {numero}. {categoria}")
        numero += 1
    while True:
        texto: str = input(f"Elegí una categoría (1-{len(CATEGORIAS)}): ").strip()
        try:
            opcion: int = int(texto)
        except ValueError:
            print("Error: ingresá el número de la categoría.")
            continue
        if opcion < 1 or opcion > len(CATEGORIAS):
            print(f"Error: el número debe estar entre 1 y {len(CATEGORIAS)}.")
            continue
        return CATEGORIAS[opcion - 1]


def pedir_descripcion() -> str:
    """Pide una descripción que no esté vacía."""
    while True:
        descripcion: str = input("Descripción: ").strip()
        if descripcion == "":
            print("Error: la descripción no puede estar vacía.")
            continue
        return descripcion


def generar_id(gastos: list[dict]) -> int:
    """Devuelve el mayor id existente + 1 (o 1 si la lista está vacía)."""
    mayor: int = 0
    for gasto in gastos:
        if gasto["id"] > mayor:
            mayor = gasto["id"]
    return mayor + 1


def pedir_mes() -> str:
    """Pide un mes en formato AAAA-MM válido."""
    while True:
        texto: str = input("Mes (AAAA-MM): ").strip()
        try:
            mes: datetime = datetime.strptime(texto, "%Y-%m")
        except ValueError:
            print("Error: mes inválido. Usá el formato AAAA-MM (ej: 2026-09).")
            continue
        return mes.strftime("%Y-%m")


# ---------- Operaciones con gastos ----------

def crear_gasto(gastos: list[dict]) -> dict:
    """Pide los datos de un gasto nuevo y lo devuelve como diccionario."""
    fecha: str = pedir_fecha()
    categoria: str = pedir_categoria()
    descripcion: str = pedir_descripcion()
    monto: float = pedir_monto()
    gasto: dict = {
        "id": generar_id(gastos),
        "fecha": fecha,
        "categoria": categoria,
        "descripcion": descripcion,
        "monto": monto,
    }
    return gasto


def mostrar_gastos(gastos: list[dict]) -> None:
    """Muestra los gastos en forma de tabla, con el total al final."""
    if len(gastos) == 0:
        print("No hay gastos para mostrar.")
        return
    print(f"{'ID':>4}  {'Fecha':<10}  {'Categoría':<11}  {'Descripción':<25}  {'Monto':>14}")
    print("-" * 71)
    total: float = 0.0
    for gasto in gastos:
        monto_texto: str = f"${gasto['monto']:,.2f}"
        print(f"{gasto['id']:>4}  {gasto['fecha']:<10}  {gasto['categoria']:<11}  "
              f"{gasto['descripcion'][:25]:<25}  {monto_texto:>14}")
        total += gasto["monto"]
    print("-" * 71)
    total_texto: str = f"${total:,.2f}"
    print(f"{len(gastos)} gasto(s){'Total:':>46}  {total_texto:>14}")


def filtrar_por_categoria(gastos: list[dict], categoria: str) -> list[dict]:
    """Devuelve los gastos de la categoría indicada."""
    resultado: list[dict] = []
    for gasto in gastos:
        if gasto["categoria"] == categoria:
            resultado.append(gasto)
    return resultado


def filtrar_por_mes(gastos: list[dict], mes: str) -> list[dict]:
    """Devuelve los gastos cuyo mes (AAAA-MM) coincide con el indicado."""
    resultado: list[dict] = []
    for gasto in gastos:
        if gasto["fecha"][:7] == mes:
            resultado.append(gasto)
    return resultado


def buscar_por_id(gastos: list[dict], id_buscado: int) -> dict | None:
    """Devuelve el gasto con el id indicado, o None si no existe."""
    for gasto in gastos:
        if gasto["id"] == id_buscado:
            return gasto
    return None


def pedir_id(gastos: list[dict]) -> int:
    """Pide un id entero hasta que corresponda a un gasto existente."""
    while True:
        texto: str = input("Id del gasto: ").strip()
        try:
            id_gasto: int = int(texto)
        except ValueError:
            print("Error: el id debe ser un número entero.")
            continue
        if buscar_por_id(gastos, id_gasto) is None:
            print(f"Error: no existe un gasto con id {id_gasto}.")
            continue
        return id_gasto


def confirmar(pregunta: str) -> bool:
    """Pregunta s/n hasta obtener una respuesta válida. Devuelve True si es 's'."""
    while True:
        respuesta: str = input(f"{pregunta} (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        if respuesta == "n":
            return False
        print("Error: respondé 's' o 'n'.")


def modificar_gasto(gasto: dict) -> bool:
    """Permite cambiar los campos de un gasto uno por uno. Devuelve True si hubo cambios."""
    hubo_cambios: bool = False
    opcion: str = ""
    while opcion != "5":
        print("\nGasto actual:")
        mostrar_gastos([gasto])
        print("¿Qué querés modificar?")
        print("1. Fecha")
        print("2. Categoría")
        print("3. Descripción")
        print("4. Monto")
        print("5. Terminar")
        opcion = input("Elegí una opción: ").strip()
        if opcion == "1":
            gasto["fecha"] = pedir_fecha()
            hubo_cambios = True
        elif opcion == "2":
            gasto["categoria"] = pedir_categoria()
            hubo_cambios = True
        elif opcion == "3":
            gasto["descripcion"] = pedir_descripcion()
            hubo_cambios = True
        elif opcion == "4":
            gasto["monto"] = pedir_monto()
            hubo_cambios = True
        elif opcion != "5":
            print("Opción inválida. Elegí un número del 1 al 5.")
    return hubo_cambios


# ---------- Indicadores ----------

def calcular_total(gastos: list[dict]) -> float:
    """Suma los montos de todos los gastos."""
    total: float = 0.0
    for gasto in gastos:
        total += gasto["monto"]
    return total


def calcular_promedio(gastos: list[dict]) -> float:
    """Devuelve el promedio por gasto (0.0 si no hay gastos)."""
    if len(gastos) == 0:
        return 0.0
    return calcular_total(gastos) / len(gastos)


def buscar_gasto_mas_alto(gastos: list[dict]) -> dict | None:
    """Recorre los gastos y devuelve el de mayor monto (None si no hay gastos)."""
    mayor: dict | None = None
    for gasto in gastos:
        if mayor is None or gasto["monto"] > mayor["monto"]:
            mayor = gasto
    return mayor


def total_por_categoria(gastos: list[dict]) -> dict[str, float]:
    """Devuelve un diccionario {categoría: total}, con todas las categorías válidas."""
    totales: dict[str, float] = {}
    for categoria in CATEGORIAS:
        totales[categoria] = 0.0
    for gasto in gastos:
        totales[gasto["categoria"]] += gasto["monto"]
    return totales


def buscar_categoria_mayor(totales: dict[str, float]) -> str | None:
    """Devuelve la categoría con mayor total (None si todos los totales son 0)."""
    categoria_mayor: str | None = None
    monto_mayor: float = 0.0
    for categoria in totales:
        if totales[categoria] > monto_mayor:
            monto_mayor = totales[categoria]
            categoria_mayor = categoria
    return categoria_mayor


def total_por_mes(gastos: list[dict]) -> dict[str, float]:
    """Devuelve un diccionario {AAAA-MM: total}, ordenado por mes."""
    totales: dict[str, float] = {}
    for gasto in gastos:
        mes: str = gasto["fecha"][:7]
        if mes in totales:
            totales[mes] += gasto["monto"]
        else:
            totales[mes] = gasto["monto"]
    ordenados: dict[str, float] = {}
    for mes in sorted(totales):
        ordenados[mes] = totales[mes]
    return ordenados


def mostrar_indicadores(gastos: list[dict]) -> None:
    """Calcula y muestra todos los indicadores."""
    total: float = calcular_total(gastos)
    promedio: float = calcular_promedio(gastos)
    mas_alto: dict | None = buscar_gasto_mas_alto(gastos)
    por_categoria: dict[str, float] = total_por_categoria(gastos)
    categoria_mayor: str | None = buscar_categoria_mayor(por_categoria)
    por_mes: dict[str, float] = total_por_mes(gastos)

    print(f"Cantidad de gastos:  {len(gastos)}")
    print(f"Total gastado:       ${total:,.2f}")
    print(f"Promedio por gasto:  ${promedio:,.2f}")
    if mas_alto is None:
        print("Gasto más alto:      (no hay gastos)")
    else:
        print(f"Gasto más alto:      ${mas_alto['monto']:,.2f} "
              f"(id {mas_alto['id']}, {mas_alto['descripcion']}, {mas_alto['fecha']})")

    print("\nTotal por categoría:")
    for categoria in por_categoria:
        monto_texto: str = f"${por_categoria[categoria]:,.2f}"
        print(f"  {categoria:<11} {monto_texto:>14}")
    if categoria_mayor is None:
        print("Categoría con mayor gasto: (no hay gastos)")
    else:
        print(f"Categoría con mayor gasto: {categoria_mayor} (${por_categoria[categoria_mayor]:,.2f})")

    print("\nTotal por mes:")
    if len(por_mes) == 0:
        print("  (no hay gastos)")
    for mes in por_mes:
        monto_texto = f"${por_mes[mes]:,.2f}"
        print(f"  {mes:<11} {monto_texto:>14}")


# ---------- Gráfico ----------

def generar_grafico(gastos: list[dict], ruta: str = ARCHIVO_GRAFICO) -> bool:
    """Genera un gráfico de barras con el total por categoría, lo guarda y lo muestra.
    Devuelve False si no hay gastos para graficar."""
    if len(gastos) == 0:
        print("No hay gastos para graficar.")
        return False

    tabla: pd.DataFrame = pd.DataFrame(gastos)
    totales: pd.Series = tabla.groupby("categoria")["monto"].sum()
    totales = totales.sort_values(ascending=False)

    figura, ejes = plt.subplots(figsize=(9, 5))
    barras = ejes.bar(totales.index, totales.values, color="#2a78d6", width=0.6)

    # Etiqueta con el monto encima de cada barra
    for barra in barras:
        altura: float = barra.get_height()
        ejes.text(barra.get_x() + barra.get_width() / 2, altura, f"${altura:,.2f}",
                  ha="center", va="bottom", fontsize=9, color="#52514e")

    ejes.set_title("Total gastado por categoría")
    ejes.set_xlabel("Categoría")
    ejes.set_ylabel("Monto total ($)")
    ejes.yaxis.set_major_formatter(lambda valor, posicion: f"${valor:,.0f}")
    ejes.grid(axis="y", color="#e0e0e0")
    ejes.set_axisbelow(True)
    ejes.spines["top"].set_visible(False)
    ejes.spines["right"].set_visible(False)

    figura.tight_layout()
    figura.savefig(ruta, dpi=120)
    print(f"Gráfico guardado en '{ruta}'. Cerrá la ventana para volver al menú.")
    plt.show()
    plt.close(figura)
    return True
