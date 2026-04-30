import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

# Conexión a la base de datos
DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(DB_URL)

def run_eda():
    print("--- Resultados de Exploración de Datos (EDA) ---")
    
    # KPI 1: Revenue Total
    query_revenue = "SELECT SUM(price) FROM order_items;"
    revenue = pd.read_sql(query_revenue, engine).iloc[0,0]
    print(f"1. Revenue Total: ${revenue:,.2f}")
    
    # KPI 2: Cantidad de Pedidos
    query_orders = "SELECT COUNT(*) FROM orders;"
    orders = pd.read_sql(query_orders, engine).iloc[0,0]
    print(f"2. Total de Pedidos: {orders}")

if __name__ == "__main__":
    run_eda()