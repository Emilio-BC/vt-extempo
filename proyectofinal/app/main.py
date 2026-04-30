from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from .db import get_db

app = FastAPI(title="Olist E-Commerce API")

@app.get("/")
def home():
    return {"status": "API Online", "project": "Olist Dashboard"}

# KPI 1: Revenue Total
@app.get("/kpi/revenue")
def get_revenue(db: Session = Depends(get_db)):
    query = text("SELECT SUM(price) FROM order_items")
    result = db.execute(query).fetchone()
    return {"kpi": "Total Revenue", "value": float(result[0]) if result[0] else 0}

# KPI 2: Ticket Promedio
@app.get("/kpi/avg-ticket")
def get_avg_ticket(db: Session = Depends(get_db)):
    query = text("SELECT AVG(price) FROM order_items")
    result = db.execute(query).fetchone()
    return {"kpi": "Average Ticket", "value": float(result[0]) if result[0] else 0}

# KPI 3: Relación de Flete (Freight Ratio)
@app.get("/kpi/freight-ratio")
def get_freight_ratio(db: Session = Depends(get_db)):
    query = text("SELECT AVG(freight_value / price) FROM order_items WHERE price > 0")
    result = db.execute(query).fetchone()
    return {"kpi": "Freight Ratio", "value": float(result[0]) if result[0] else 0}

# KPI 4: Volumen de Pedidos
@app.get("/kpi/orders-count")
def get_orders_count(db: Session = Depends(get_db)):
    query = text("SELECT COUNT(*) FROM orders")
    result = db.execute(query).fetchone()
    return {"kpi": "Order Volume", "value": int(result[0]) if result[0] else 0}
