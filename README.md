# TP1 - App de Gastos Personales en Python

Aplicación sencilla para registrar y analizar gastos personales.

El proyecto fue realizado para el Trabajo Práctico 1 de **Elementos de Programación IA y Low Code**.

## Objetivo

Permitir que una persona pueda:

- Registrar gastos.
- Ver los gastos guardados.
- Modificar un gasto.
- Eliminar un gasto.
- Filtrar por categoría.
- Calcular tres indicadores:
  - total gastado;
  - promedio por gasto;
  - gasto mayor.
- Generar un gráfico de gastos por categoría.
- Guardar y recuperar la información desde un archivo JSON.

## Archivos

- `main.py`: interfaz gráfica y flujo principal.
- `funciones.py`: funciones que trabajan con los datos.
- `datos.json`: gastos guardados.
- `analisis.ipynb`: análisis sencillo con pandas y Matplotlib.
- `grafico.png`: ejemplo del gráfico generado.
- `requirements.txt`: bibliotecas necesarias.
- `prompts.txt`: registro del uso de inteligencia artificial.

## Tecnologías utilizadas

- Python
- Tkinter
- JSON
- pandas
- Matplotlib

Tkinter viene incluido con la instalación normal de Python para Windows.

## Instalación

1. Instalar Python.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Instalar las bibliotecas:

```bash
pip install -r requirements.txt
```

## Ejecutar la aplicación

Desde la carpeta del proyecto:

```bash
python main.py
```

## Cómo usarla

1. Escribir la fecha con formato `AAAA-MM-DD`.
2. Elegir una categoría.
3. Escribir una descripción.
4. Escribir el monto.
5. Presionar **Agregar gasto**.

Para modificar:

1. Seleccionar un gasto de la lista.
2. Presionar **Cargar seleccionado**.
3. Cambiar los datos.
4. Presionar **Modificar**.

Para eliminar:

1. Seleccionar un gasto.
2. Presionar **Eliminar**.

Para filtrar:

1. Elegir una categoría en la parte inferior.
2. Presionar **Filtrar**.
3. Con **Mostrar todos** se quita el filtro.

El botón **Ver gráfico** genera `grafico.png` y muestra un gráfico de barras.

## Decisiones principales

Se eligió una solución intencionalmente sencilla.

- Los gastos se guardan como una **lista de diccionarios**.
- Se utiliza **JSON** porque permite guardar esa estructura de manera directa.
- `main.py` contiene la interfaz.
- `funciones.py` contiene la lógica reutilizable.
- Se utiliza **Tkinter** porque forma parte de Python y permite crear una interfaz sin agregar un framework web.
- Se utilizaron funciones normales en lugar de clases para mantener el código fácil de explicar.
- Se utiliza pandas solamente para organizar los datos del análisis y para agrupar los montos del gráfico.
- Matplotlib genera el gráfico de barras.

## Contenidos de Python presentes

El proyecto incluye:

- Variables y distintos tipos de datos.
- Condiciones `if`.
- Repeticiones `for`.
- Listas y diccionarios.
- Funciones propias con anotaciones de tipo.
- Manejo de errores con `try` y `except`.
- Dos módulos `.py`.
- Lectura y escritura de JSON.
- pandas.
- Matplotlib.

## Pruebas realizadas

Se comprobaron los siguientes casos:

- Cargar los datos existentes desde `datos.json`.
- Agregar un gasto válido.
- Intentar ingresar un monto que no es un número.
- Intentar ingresar una fecha con formato incorrecto.
- Modificar un gasto existente.
- Eliminar un gasto.
- Filtrar por categoría.
- Calcular total, promedio y gasto mayor.
- Generar el gráfico por categoría.

## Notebook

Para abrir el análisis:

```bash
jupyter notebook analisis.ipynb
```

También puede abrirse desde Visual Studio Code si tiene soporte para notebooks.
