import os
from dotenv import load_dotenv

# Esto busca el archivo .env en la carpeta donde estás parado
load_dotenv()

class Settings:
    PROJECT_NAME: str = "Olist E-Commerce API"
    
    # Usamos .get() para dar valores por defecto si el .env falla
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASS = os.getenv('DB_PASSWORD', 'password')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432') # Por defecto 5432
    DB_NAME = os.getenv('DB_NAME', 'olist_db')

    DATABASE_URL: str = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

settings = Settings()