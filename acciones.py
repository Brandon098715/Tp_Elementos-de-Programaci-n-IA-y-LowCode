"""Acciones que se ejecutan cuando el usuario usa la interfaz."""

import tkinter as tk
from tkinter import messagebox

from datos import cargar_gastos, guardar_gastos
from funciones import (
    agregar_gasto,
    calcular_indicadores,
    eliminar_gasto,
    filtrar_por_categoria,
    modificar_gasto,
    validar_fecha,
)
from graficos import crear_grafico


# Los gastos se mantienen en memoria como una lista de diccionarios.
gastos = cargar_gastos()
gastos_visibles = gastos.copy()

# Estas variables guardarán referencias a los controles de la ventana.
entrada_fecha = None
categoria = None
entrada_descripcion = None
entrada_monto = None
lista_gastos = None
filtro_categoria = None
etiqueta_total = None
etiqueta_promedio = None
etiqueta_mayor = None


def configurar_controles(
    campo_fecha,
    campo_categoria,
    campo_descripcion,
    campo_monto,
    lista,
    filtro,
    total,
    promedio,
    mayor,
) -> None:
    """Recibe los controles creados en interfaz.py para poder usarlos."""

    global entrada_fecha
    global categoria
    global entrada_descripcion
    global entrada_monto
    global lista_gastos
    global filtro_categoria
    global etiqueta_total
    global etiqueta_promedio
    global etiqueta_mayor

    entrada_fecha = campo_fecha
    categoria = campo_categoria
    entrada_descripcion = campo_descripcion
    entrada_monto = campo_monto
    lista_gastos = lista
    filtro_categoria = filtro
    etiqueta_total = total
    etiqueta_promedio = promedio
    etiqueta_mayor = mayor


def actualizar_lista(lista: list) -> None:
    """Muestra en pantalla los gastos recibidos."""

    global gastos_visibles

    gastos_visibles = lista
    lista_gastos.delete(0, tk.END)

    for gasto in lista:
        texto = (
            f'{gasto["id"]} | {gasto["fecha"]} | {gasto["categoria"]} | '
            f'{gasto["descripcion"]} | ${gasto["monto"]:.2f}'
        )
        lista_gastos.insert(tk.END, texto)

    actualizar_indicadores()


def actualizar_indicadores() -> None:
    """Actualiza total, promedio y gasto mayor."""

    total, promedio, mayor = calcular_indicadores(gastos)

    etiqueta_total.config(text=f"Total gastado: ${total:.2f}")
    etiqueta_promedio.config(text=f"Promedio: ${promedio:.2f}")
    etiqueta_mayor.config(text=f"Gasto mayor: ${mayor:.2f}")


def limpiar_campos() -> None:
    """Vacía los campos del formulario."""

    entrada_fecha.delete(0, tk.END)
    entrada_descripcion.delete(0, tk.END)
    entrada_monto.delete(0, tk.END)
    categoria.set("Comida")


def obtener_datos_formulario() -> tuple:
    """Lee y valida los datos escritos por el usuario."""

    fecha = entrada_fecha.get().strip()
    categoria_elegida = categoria.get()
    descripcion = entrada_descripcion.get().strip()
    monto_texto = entrada_monto.get().strip()

    if fecha == "" or descripcion == "" or monto_texto == "":
        raise ValueError("Todos los campos son obligatorios.")

    if not validar_fecha(fecha):
        raise ValueError("La fecha debe tener formato AAAA-MM-DD.")

    try:
        monto = float(monto_texto)
    except ValueError:
        raise ValueError("El monto debe ser un número.")

    if monto <= 0:
        raise ValueError("El monto debe ser mayor que cero.")

    return fecha, categoria_elegida, descripcion, monto


def guardar_nuevo_gasto() -> None:
    """Agrega un gasto nuevo y guarda los cambios."""

    try:
        fecha, categoria_elegida, descripcion, monto = obtener_datos_formulario()
    except ValueError as error:
        messagebox.showerror("Error", str(error))
        return

    agregar_gasto(gastos, fecha, categoria_elegida, descripcion, monto)
    guardar_gastos(gastos)

    actualizar_lista(gastos)
    limpiar_campos()
    messagebox.showinfo("Listo", "El gasto fue agregado.")


def cargar_seleccionado() -> None:
    """Carga en el formulario el gasto seleccionado."""

    seleccion = lista_gastos.curselection()

    if len(seleccion) == 0:
        messagebox.showwarning("Atención", "Primero seleccioná un gasto.")
        return

    gasto = gastos_visibles[seleccion[0]]

    entrada_fecha.delete(0, tk.END)
    entrada_fecha.insert(0, gasto["fecha"])
    categoria.set(gasto["categoria"])
    entrada_descripcion.delete(0, tk.END)
    entrada_descripcion.insert(0, gasto["descripcion"])
    entrada_monto.delete(0, tk.END)
    entrada_monto.insert(0, str(gasto["monto"]))


def guardar_modificacion() -> None:
    """Modifica el gasto seleccionado y guarda los cambios."""

    seleccion = lista_gastos.curselection()

    if len(seleccion) == 0:
        messagebox.showwarning("Atención", "Primero seleccioná un gasto.")
        return

    id_gasto = gastos_visibles[seleccion[0]]["id"]

    try:
        fecha, categoria_elegida, descripcion, monto = obtener_datos_formulario()
    except ValueError as error:
        messagebox.showerror("Error", str(error))
        return

    modificar_gasto(
        gastos,
        id_gasto,
        fecha,
        categoria_elegida,
        descripcion,
        monto,
    )

    guardar_gastos(gastos)
    actualizar_lista(gastos)
    limpiar_campos()
    messagebox.showinfo("Listo", "El gasto fue modificado.")


def borrar_seleccionado() -> None:
    """Elimina el gasto seleccionado y guarda los cambios."""

    seleccion = lista_gastos.curselection()

    if len(seleccion) == 0:
        messagebox.showwarning("Atención", "Primero seleccioná un gasto.")
        return

    id_gasto = gastos_visibles[seleccion[0]]["id"]

    confirmar = messagebox.askyesno(
        "Confirmar",
        "¿Querés eliminar el gasto seleccionado?",
    )

    if confirmar:
        eliminar_gasto(gastos, id_gasto)
        guardar_gastos(gastos)
        actualizar_lista(gastos)
        limpiar_campos()


def aplicar_filtro() -> None:
    """Filtra los gastos usando la categoría seleccionada."""

    categoria_buscada = filtro_categoria.get()

    if categoria_buscada == "Todas":
        actualizar_lista(gastos)
    else:
        resultado = filtrar_por_categoria(gastos, categoria_buscada)
        actualizar_lista(resultado)


def mostrar_todos() -> None:
    """Quita el filtro y vuelve a mostrar todos los gastos."""

    filtro_categoria.set("Todas")
    actualizar_lista(gastos)


def ver_grafico() -> None:
    """Genera y muestra el gráfico de gastos."""

    if len(gastos) == 0:
        messagebox.showwarning("Atención", "No hay gastos para graficar.")
        return

    crear_grafico(gastos)
