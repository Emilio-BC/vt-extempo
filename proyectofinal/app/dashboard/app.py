from dash import Dash, html, dcc
import requests

app = Dash(__name__)

# URL de tu API (Asegúrate de que uvicorn siga encendido)
API_URL = "http://127.0.0.1:8000/kpi"

def get_kpi_value(endpoint):
    try:
        r = requests.get(f"{API_URL}/{endpoint}")
        return r.json().get("value", 0)
    except:
        return 0

app.layout = html.Div([
    html.H1("Olist E-Commerce Performance", style={'textAlign': 'center', 'color': '#2c3e50'}),
    
    html.Div([
        # Tarjeta 1: Revenue
        html.Div([
            html.H3("Ingresos Totales"),
            html.P(f"${get_kpi_value('revenue'):,.2f}", style={'fontSize': '24px', 'fontWeight': 'bold'})
        ], className="card"),
        
        # Tarjeta 2: Pedidos
        html.Div([
            html.H3("Volumen de Pedidos"),
            html.P(f"{get_kpi_value('orders-count'):,}", style={'fontSize': '24px', 'fontWeight': 'bold'})
        ], className="card"),
    ], style={'display': 'flex', 'justifyContent': 'space-around', 'padding': '20px'})
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
    