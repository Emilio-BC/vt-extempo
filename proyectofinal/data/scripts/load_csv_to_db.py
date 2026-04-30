import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

# Configuración de conexión
DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(DB_URL)

def load_data():
    # Rutas de tus CSV descargados de Kaggle
    files = {
        'orders': 'data/olist_orders_dataset.csv',
        'order_items': 'data/olist_order_items_dataset.csv'
    }
    
    for table_name, file_path in files.items():
        print(f"Cargando {table_name}...")
        df = pd.read_csv(file_path)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"✅ {table_name} cargada con éxito.")

if __name__ == "__main__":
    load_data()
    