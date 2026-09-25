# TP1 · App de Gastos Personales en Python

Aplicación de consola para registrar gastos personales, consultarlos, calcular indicadores y graficarlos. Los datos se guardan en `datos.json`.

## Archivos

| Archivo | Contenido |
|---|---|
| `main.py` | Menú y flujo principal |
| `funciones.py` | Lógica reutilizable (carga/guardado, validaciones, indicadores, gráfico) |
| `datos.json` | Lista de gastos |
| `analisis.ipynb` | Análisis de los datos con pandas y matplotlib |
| `requirements.txt` | Dependencias |

## Instalación

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Uso

```
python main.py
```

## Modelo de datos

Cada gasto es un diccionario:

```python
{"id": 1, "fecha": "2026-09-20", "categoria": "Comida", "descripcion": "Supermercado", "monto": 35000.0}
```

Categorías válidas: Comida, Transporte, Servicios, Ocio, Salud, Otros.

## Menú

1. Registrar gasto
2. Listar gastos
3. Filtrar por categoría
4. Filtrar por mes (AAAA-MM)
5. Modificar gasto (por id)
6. Eliminar gasto (por id, con confirmación)
7. Ver indicadores
8. Generar gráfico por categoría
9. Salir
