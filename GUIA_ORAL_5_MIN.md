# Guía rápida para el oral de 5 minutos

Este archivo es material de apoyo. No hace falta leerlo textual.

## 1. Qué hace el programa

"Es una aplicación de gastos personales. Permite cargar, consultar, modificar, eliminar y filtrar gastos. Los datos quedan guardados en un archivo JSON. También calcula tres indicadores y genera un gráfico."

## 2. Cómo están organizados los archivos

"Separé el programa en dos módulos principales. `main.py` tiene la interfaz y el flujo del programa. `funciones.py` contiene las funciones que trabajan con los datos."

## 3. Cómo se representa un gasto

"Cada gasto es un diccionario."

Ejemplo:

```python
{
    "id": 1,
    "fecha": "2026-09-20",
    "categoria": "Comida",
    "descripcion": "Supermercado",
    "monto": 18500.0
}
```

"Todos los diccionarios se guardan dentro de una lista."

## 4. Para qué sirve JSON

"`datos.json` permite que los gastos no desaparezcan cuando cierro el programa. Al iniciar uso `json.load` para leer y al guardar uso `json.dump`."

## 5. Ejemplo de repetición

"En varias funciones uso `for` para recorrer la lista de gastos. Por ejemplo, para buscar un ID o calcular el total."

## 6. Ejemplo de condición

"Uso `if` para comparar el ID, filtrar una categoría o verificar si no hay gastos."

## 7. Manejo de errores

"Uso `try` y `except` al leer JSON, validar una fecha y convertir el monto escrito por el usuario a número. De esa manera una entrada incorrecta no cierra el programa."

## 8. Los tres indicadores

- Total gastado.
- Promedio por gasto.
- Gasto mayor.

"La función `calcular_indicadores` recorre los gastos, acumula el total y busca el monto más alto. Después calcula el promedio."

## 9. pandas

"Con pandas convierto la lista en un DataFrame. Después agrupo los gastos por categoría y sumo los montos."

## 10. Matplotlib

"Matplotlib toma esos totales y crea el gráfico de barras. El gráfico también se guarda en `grafico.png`."

## 11. Tkinter

"Tkinter es la biblioteca que usé para hacer la interfaz. Los controles principales son etiquetas, campos de texto, botones, listas y menús desplegables."

## 12. Uso de IA

"Usé IA como asistencia para proponer la interfaz y simplificar el código. Elegí mantener una solución básica porque necesitaba poder comprender y explicar cada parte. Los prompts están documentados en `prompts.txt`."
