import tkinter as tk
from tkinter import messagebox

from funciones import (
    cargar_gastos,
    guardar_gastos,
    agregar_gasto,
    modificar_gasto,
    eliminar_gasto,
    filtrar_por_categoria,
    calcular_indicadores,
    crear_grafico,
    validar_fecha,
)

# Cargamos los datos al iniciar el programa.
gastos = cargar_gastos()

# Esta lista guarda los gastos que se ven en pantalla.
# Puede contener todos los gastos o solamente los filtrados.
gastos_visibles = gastos.copy()


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
    """Agrega un gasto nuevo a la lista y al archivo JSON."""
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

    posicion = seleccion[0]
    gasto = gastos_visibles[posicion]

    entrada_fecha.delete(0, tk.END)
    entrada_fecha.insert(0, gasto["fecha"])

    categoria.set(gasto["categoria"])

    entrada_descripcion.delete(0, tk.END)
    entrada_descripcion.insert(0, gasto["descripcion"])

    entrada_monto.delete(0, tk.END)
    entrada_monto.insert(0, str(gasto["monto"]))


def guardar_modificacion() -> None:
    """Modifica el gasto seleccionado usando los datos del formulario."""
    seleccion = lista_gastos.curselection()

    if len(seleccion) == 0:
        messagebox.showwarning("Atención", "Primero seleccioná un gasto.")
        return

    posicion = seleccion[0]
    id_gasto = gastos_visibles[posicion]["id"]

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
    """Elimina el gasto seleccionado."""
    seleccion = lista_gastos.curselection()

    if len(seleccion) == 0:
        messagebox.showwarning("Atención", "Primero seleccioná un gasto.")
        return

    posicion = seleccion[0]
    id_gasto = gastos_visibles[posicion]["id"]

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
    """Filtra los gastos por categoría."""
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
    """Genera y muestra el gráfico de gastos por categoría."""
    if len(gastos) == 0:
        messagebox.showwarning("Atención", "No hay gastos para graficar.")
        return

    crear_grafico(gastos)


# -------------------------
# INTERFAZ GRÁFICA
# -------------------------

ventana = tk.Tk()
ventana.title("Control de gastos personales")
ventana.geometry("850x620")

titulo = tk.Label(
    ventana,
    text="CONTROL DE GASTOS PERSONALES",
    font=("Arial", 16, "bold"),
)
titulo.grid(row=0, column=0, columnspan=4, pady=15)

# Formulario
tk.Label(ventana, text="Fecha (AAAA-MM-DD):").grid(
    row=1, column=0, padx=5, pady=5, sticky="e"
)
entrada_fecha = tk.Entry(ventana, width=20)
entrada_fecha.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Categoría:").grid(
    row=1, column=2, padx=5, pady=5, sticky="e"
)
categoria = tk.StringVar(value="Comida")
opciones_categoria = ["Comida", "Transporte", "Servicios", "Ocio", "Otros"]
menu_categoria = tk.OptionMenu(ventana, categoria, *opciones_categoria)
menu_categoria.grid(row=1, column=3, padx=5, pady=5, sticky="w")

tk.Label(ventana, text="Descripción:").grid(
    row=2, column=0, padx=5, pady=5, sticky="e"
)
entrada_descripcion = tk.Entry(ventana, width=30)
entrada_descripcion.grid(row=2, column=1, padx=5, pady=5)

tk.Label(ventana, text="Monto:").grid(
    row=2, column=2, padx=5, pady=5, sticky="e"
)
entrada_monto = tk.Entry(ventana, width=20)
entrada_monto.grid(row=2, column=3, padx=5, pady=5, sticky="w")

boton_agregar = tk.Button(
    ventana,
    text="Agregar gasto",
    width=18,
    command=guardar_nuevo_gasto,
)
boton_agregar.grid(row=3, column=0, padx=5, pady=10)

boton_cargar = tk.Button(
    ventana,
    text="Cargar seleccionado",
    width=18,
    command=cargar_seleccionado,
)
boton_cargar.grid(row=3, column=1, padx=5, pady=10)

boton_modificar = tk.Button(
    ventana,
    text="Modificar",
    width=18,
    command=guardar_modificacion,
)
boton_modificar.grid(row=3, column=2, padx=5, pady=10)

boton_eliminar = tk.Button(
    ventana,
    text="Eliminar",
    width=18,
    command=borrar_seleccionado,
)
boton_eliminar.grid(row=3, column=3, padx=5, pady=10)

# Lista de gastos
tk.Label(ventana, text="Gastos registrados:").grid(
    row=4, column=0, columnspan=4, pady=(10, 5)
)

lista_gastos = tk.Listbox(ventana, width=105, height=14)
lista_gastos.grid(row=5, column=0, columnspan=4, padx=15, pady=5)

# Filtros
tk.Label(ventana, text="Filtrar por categoría:").grid(
    row=6, column=0, padx=5, pady=10, sticky="e"
)

filtro_categoria = tk.StringVar(value="Todas")
opciones_filtro = ["Todas"] + opciones_categoria
menu_filtro = tk.OptionMenu(ventana, filtro_categoria, *opciones_filtro)
menu_filtro.grid(row=6, column=1, padx=5, pady=10)

boton_filtrar = tk.Button(
    ventana,
    text="Filtrar",
    width=15,
    command=aplicar_filtro,
)
boton_filtrar.grid(row=6, column=2, padx=5, pady=10)

boton_todos = tk.Button(
    ventana,
    text="Mostrar todos",
    width=15,
    command=mostrar_todos,
)
boton_todos.grid(row=6, column=3, padx=5, pady=10)

# Indicadores
etiqueta_total = tk.Label(ventana, text="Total gastado: $0")
etiqueta_total.grid(row=7, column=0, padx=5, pady=10)

etiqueta_promedio = tk.Label(ventana, text="Promedio: $0")
etiqueta_promedio.grid(row=7, column=1, padx=5, pady=10)

etiqueta_mayor = tk.Label(ventana, text="Gasto mayor: $0")
etiqueta_mayor.grid(row=7, column=2, padx=5, pady=10)

boton_grafico = tk.Button(
    ventana,
    text="Ver gráfico",
    width=15,
    command=ver_grafico,
)
boton_grafico.grid(row=7, column=3, padx=5, pady=10)

# Mostramos los gastos al abrir la aplicación.
actualizar_lista(gastos)

ventana.mainloop()
