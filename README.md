S1: Planning - Reporte Ejecutivo 

1. Introducción y Contexto 

Proyecto: Dashboard de Inteligencia de Negocios para E-Commerce (Olist Brazil).  

Contexto de Negocio: Olist es un marketplace brasileño que conecta pequeñas empresas con grandes canales de venta. El objetivo es analizar el rendimiento de las ventas para optimizar la toma de decisiones logística y comercial.  

Contexto del Dataset: Se utilizarán tablas relacionadas que contienen información de pedidos (orders), productos (order_items), clientes y geolocalización, permitiendo un análisis 360° del flujo de venta.  

2. Descripción de Tablas y Modelo ER 

Trabajaremos principalmente con dos tablas núcleo: 

olist_orders_dataset: Contiene el ID del pedido, ID del cliente, estatus y marcas de tiempo (creación, entrega, etc.).  

olist_order_items_dataset: Contiene el detalle de cada artículo, precio, valor del flete y el ID del vendedor.  

Diagrama ER Sugerido: Una relación 1:N entre orders y order_items a través de la llave order_id.  


Pregunta de Negocio 

KPI Sugerido 

Tabla.Columna  

¿Cuál es la facturación total del periodo? 

Revenue Total 

order_items.price (SUM) 

¿Qué tan costoso es el envío respecto al producto? 

Freight Ratio 

order_items.freight_value / price 

¿Cuál es el volumen de ventas por mes? 

Order Volume 

orders.order_purchase_timestamp 

¿Cuál es el valor promedio de compra? 

Ticket Promedio 

order_items.price (AVG) 

