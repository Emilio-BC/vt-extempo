import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos del ejercicio 2.2[cite: 2]
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
meals = [40139, 127020, 168193, 153115, 202102, 232897, 277912, 205350, 233389, 232797]
df_meals = pd.DataFrame({'Year': years, 'Meals': meals})

# Configuración de la figura para los 3 pasos solicitados
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# PASO 1: Mapa de calor (Heatmap)[cite: 2]
# Reorganizamos los datos para el heatmap
sns.heatmap(df_meals[['Meals']], annot=True, fmt="d", cmap="YlGnBu", ax=axs[0], cbar=False)
axs[0].set_title('Paso 1: Heatmap')

# PASO 2: Gráfico de barras[cite: 2]
axs[1].bar(df_meals['Year'], df_meals['Meals'], color='skyblue')
axs[1].set_title('Paso 2: Gráfico de Barras')
axs[1].set_xticks(years)
axs[1].tick_params(axis='x', rotation=45)

# PASO 3: Gráfico de líneas[cite: 2]
axs[2].plot(df_meals['Year'], df_meals['Meals'], marker='o', color='green', linewidth=2)
axs[2].set_title('Paso 3: Gráfico de Líneas')
axs[2].set_xticks(years)
axs[2].tick_params(axis='x', rotation=45)
axs[2].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
