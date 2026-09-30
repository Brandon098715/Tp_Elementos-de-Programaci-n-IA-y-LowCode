"""Construcción de la interfaz gráfica con Tkinter."""

import tkinter as tk

import acciones


CATEGORIAS = ["Comida", "Transporte", "Servicios", "Ocio", "Otros"]


def iniciar_aplicacion() -> None:
    """Crea todos los controles de la ventana e inicia Tkinter."""

    ventana = tk.Tk()
    ventana.title("Control de gastos personales")
    ventana.geometry("860x640")

    # Título
    tk.Label(
        ventana,
        text="CONTROL DE GASTOS PERSONALES",
        font=("Arial", 16, "bold"),
    ).grid(row=0, column=0, columnspan=4, pady=15)

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
    tk.OptionMenu(ventana, categoria, *CATEGORIAS).grid(
        row=1, column=3, padx=5, pady=5, sticky="w"
    )

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

    # Botones principales
    tk.Button(
        ventana,
        text="Agregar gasto",
        width=18,
        command=acciones.guardar_nuevo_gasto,
    ).grid(row=3, column=0, padx=5, pady=10)

    tk.Button(
        ventana,
        text="Cargar seleccionado",
        width=18,
        command=acciones.cargar_seleccionado,
    ).grid(row=3, column=1, padx=5, pady=10)

    tk.Button(
        ventana,
        text="Modificar",
        width=18,
        command=acciones.guardar_modificacion,
    ).grid(row=3, column=2, padx=5, pady=10)

    tk.Button(
        ventana,
        text="Eliminar",
        width=18,
        command=acciones.borrar_seleccionado,
    ).grid(row=3, column=3, padx=5, pady=10)

    # Lista de gastos
    tk.Label(
        ventana,
        text="ID | Fecha | Categoría | Descripción | Monto",
    ).grid(row=4, column=0, columnspan=4, pady=(10, 5))

    lista_gastos = tk.Listbox(ventana, width=105, height=14)
    lista_gastos.grid(row=5, column=0, columnspan=4, padx=15, pady=5)

    # Filtros
    tk.Label(ventana, text="Filtrar por categoría:").grid(
        row=6, column=0, padx=5, pady=10, sticky="e"
    )

    filtro_categoria = tk.StringVar(value="Todas")
    opciones_filtro = ["Todas"] + CATEGORIAS
    tk.OptionMenu(ventana, filtro_categoria, *opciones_filtro).grid(
        row=6, column=1, padx=5, pady=10
    )

    tk.Button(
        ventana,
        text="Filtrar",
        width=15,
        command=acciones.aplicar_filtro,
    ).grid(row=6, column=2, padx=5, pady=10)

    tk.Button(
        ventana,
        text="Mostrar todos",
        width=15,
        command=acciones.mostrar_todos,
    ).grid(row=6, column=3, padx=5, pady=10)

    # Indicadores
    etiqueta_total = tk.Label(ventana, text="Total gastado: $0")
    etiqueta_total.grid(row=7, column=0, padx=5, pady=10)

    etiqueta_promedio = tk.Label(ventana, text="Promedio: $0")
    etiqueta_promedio.grid(row=7, column=1, padx=5, pady=10)

    etiqueta_mayor = tk.Label(ventana, text="Gasto mayor: $0")
    etiqueta_mayor.grid(row=7, column=2, padx=5, pady=10)

    tk.Button(
        ventana,
        text="Ver gráfico",
        width=15,
        command=acciones.ver_grafico,
    ).grid(row=7, column=3, padx=5, pady=10)

    # Entregamos a acciones.py los controles que necesita leer o actualizar.
    acciones.configurar_controles(
        entrada_fecha,
        categoria,
        entrada_descripcion,
        entrada_monto,
        lista_gastos,
        filtro_categoria,
        etiqueta_total,
        etiqueta_promedio,
        etiqueta_mayor,
    )

    acciones.actualizar_lista(acciones.gastos)
    ventana.mainloop()
