import pandas as pd
import plotly.express as px
import os

# 1. DATOS DE PRUEBA
data = {
    'Fecha Venta': pd.to_datetime(['2025-11-01', '2025-11-15', '2025-12-01', '2025-12-24']),
    'Total (MXN)': [1500, 2200, 3500, 5000],
    'Unidades': [1, 2, 3, 5],
    'Ventas por publicidad': ['Si', 'No', 'No', 'Si'],
    'Estado': ['Yucatán', 'Jalisco', 'Nuevo León', 'Querétaro'],
    'Titulo de la publicación': ['Moneda Plata', 'Onza Libertad', 'Moneda Plata', 'Set Centenario']
}
df = pd.DataFrame(data)

# 2. CREACIÓN DE GRÁFICOS
fig = px.line(df, x='Fecha Venta', y='Total (MXN)', color='Ventas por publicidad', title='Dashboard Numismática México')

# 3. GUARDADO CON RUTA ABSOLUTA
# Forzamos a que se guarde en tu carpeta de trabajo
ruta_final = r"C:\Users\usuario\data\vs tools\extempo\Dashboard_Numismatica_Mexico.html"
fig.write_html(ruta_final)

print(f"--- PROCESO COMPLETADO ---")
print(f"El archivo DEBE estar aquí: {ruta_final}")
