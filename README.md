# TP1 - App de Gastos Personales en Python

Aplicación sencilla para registrar, consultar y analizar gastos personales.

El proyecto fue realizado para el Trabajo Práctico 1 de **Elementos de Programación IA y Low Code**.

## Objetivo

La aplicación permite:

- Registrar gastos.
- Ver los gastos guardados.
- Modificar gastos.
- Eliminar gastos.
- Filtrar por categoría.
- Calcular tres indicadores: total gastado, promedio por gasto y gasto mayor.
- Generar un gráfico de gastos por categoría.
- Guardar y recuperar la información desde un archivo JSON.

## Organización del proyecto

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Inicia la aplicación. |
| `interfaz.py` | Construye la ventana, los campos y los botones de Tkinter. |
| `acciones.py` | Contiene las acciones que se ejecutan al usar los botones. |
| `funciones.py` | Contiene la lógica para validar, agregar, modificar, eliminar, filtrar y calcular indicadores. |
| `datos.py` | Lee y guarda `datos.json`. |
| `graficos.py` | Usa pandas y Matplotlib para generar el gráfico. |
| `pruebas.py` | Ejecuta pruebas simples de las funciones principales. |
| `analisis.ipynb` | Analiza los datos con pandas y genera un gráfico. |
| `datos.json` | Guarda los gastos. |
| `grafico.png` | Gráfico generado a partir de los datos de ejemplo. |
| `prompts.txt` | Documenta el uso de inteligencia artificial. |
| `requirements.txt` | Bibliotecas externas necesarias. |

## Estructura de los datos

Cada gasto se representa con un diccionario:

```python
{
    "id": 1,
    "fecha": "2026-09-20",
    "categoria": "Comida",
    "descripcion": "Supermercado",
    "monto": 18500.0
}
```

Todos los gastos se guardan dentro de una lista. Esa lista se guarda en `datos.json` para que la información no se pierda cuando se cierra el programa.

## Instalación

Tkinter viene incluido con la instalación normal de Python para Windows.

En Windows, abrir PowerShell dentro de la carpeta del proyecto y ejecutar:

```powershell
py -m pip install -r requirements.txt
```

## Ejecutar la aplicación

```powershell
py main.py
```

## Ejecutar las pruebas

```powershell
py pruebas.py
```

El resultado esperado es:

```text
OK   - Agregar gasto
OK   - Modificar gasto
OK   - Filtrar por categoría
OK   - Calcular indicadores
OK   - Validar fecha correcta
OK   - Detectar fecha incorrecta
OK   - Eliminar gasto

Pruebas finalizadas.
```

## Abrir el notebook

```powershell
py -m jupyter notebook analisis.ipynb
```

## Cómo se cumplen las consignas

| Consigna | Dónde se demuestra |
|---|---|
| Variables y tipos de datos | En todos los módulos, especialmente en los datos de cada gasto. |
| Condiciones | `if` en validaciones, filtros, búsqueda de IDs e interfaz. |
| Estructuras repetitivas | `for` para recorrer la lista de gastos. |
| Listas y diccionarios | La lista `gastos` contiene un diccionario por cada registro. |
| Cuatro o más funciones propias | `funciones.py`, `datos.py`, `graficos.py`, `acciones.py` e `interfaz.py`. |
| Anotaciones de tipo | Parámetros y retornos de las funciones. |
| `try` y `except` | Validación de fecha, conversión del monto y lectura del JSON. |
| Dos o más módulos `.py` | El proyecto está separado en varios módulos con responsabilidades distintas. |
| JSON o CSV | `datos.py` lee y guarda `datos.json`. |
| pandas | `graficos.py` y `analisis.ipynb`. |
| Matplotlib | `graficos.py` y `analisis.ipynb`. |
| Cargar o recuperar información | Los datos se recuperan desde `datos.json` al iniciar. |
| Validar datos | Fecha, monto y campos obligatorios. |
| Consultar, filtrar o modificar | La interfaz permite filtrar, modificar y eliminar. |
| Tres indicadores | Total, promedio y gasto mayor. |
| Visualización | Gráfico de barras por categoría. |

## Decisiones principales

Se eligió una solución intencionalmente sencilla para que todo el código pueda ser comprendido y explicado.

- Se usa **Tkinter** porque viene incluido con Python y permite crear una interfaz sin un framework web.
- Se usa **JSON** porque guarda directamente listas y diccionarios.
- Se separaron las responsabilidades en archivos pequeños.
- `interfaz.py` construye la pantalla y `acciones.py` responde a los botones. Para mantener el código básico se usan variables simples de módulo en lugar de clases.
- No se utilizaron clases ni una base de datos porque no eran necesarias para la consigna.
- pandas se utiliza para organizar y agrupar datos.
- Matplotlib se utiliza únicamente para generar el gráfico.

## Pruebas y corrección

Las funciones principales se prueban en `pruebas.py` sin modificar `datos.json`.

Además se probaron manualmente:

- carga inicial de datos;
- alta de un gasto;
- monto no numérico;
- fecha incorrecta;
- modificación;
- eliminación;
- filtro por categoría;
- indicadores;
- generación del gráfico.

## Uso de inteligencia artificial

El uso de IA está documentado en `prompts.txt`.

Se registraron los prompts utilizados, la respuesta recibida, la decisión tomada y la forma en que se comprobó el funcionamiento del código.
