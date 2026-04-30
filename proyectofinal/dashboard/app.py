from dash import Dash, html, dcc
import requests
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# URL de tu API de FastAPI (S3) - Asegúrate de que uvicorn esté corriendo
API_URL = "http://127.0.0.1:8000/kpi"

def get_kpi(endpoint):
    try:
        r = requests.get(f"{API_URL}/{endpoint}")
        return r.json().get("value", 0)
    except:
        return 0

# Ejemplo de datos para una gráfica (S4 pide visualizaciones)
df_ejemplo = pd.DataFrame({
    "Categoría": ["Electrónicos", "Hogar", "Moda", "Belleza"],
    "Ventas": [450, 300, 200, 150]
})
fig = px.bar(df_ejemplo, x="Categoría", y="Ventas", title="Ventas por Categoría (Ejemplo)")

app.layout = html.Div([
    html.H1("Dashboard Olist - E-Commerce Performance", style={'textAlign': 'center', 'fontFamily': 'Arial'}),
    
    # Tarjetas de KPIs
    html.Div([
        html.Div([
            html.H3("Ingresos Totales"),
            html.P(f"${get_kpi('revenue'):,.2f}", style={'fontSize': '24px', 'color': '#27ae60'})
        ], style={'padding': '20px', 'border': '1px solid #ddd', 'borderRadius': '10px', 'width': '30%'}),
        
        html.Div([
            html.H3("Pedidos Totales"),
            html.P(f"{get_kpi('orders-count'):,}", style={'fontSize': '24px', 'color': '#2980b9'})
        ], style={'padding': '20px', 'border': '1px solid #ddd', 'borderRadius': '10px', 'width': '30%'})
    ], style={'display': 'flex', 'justifyContent': 'space-around', 'marginBottom': '40px'}),

    # Gráfico
    html.Div([
        dcc.Graph(figure=fig)
    ], style={'width': '80%', 'margin': 'auto'})
])

if __name__ == '__main__':
    # Cambiamos run_server por run para evitar el error
    app.run(debug=True, port=8050)