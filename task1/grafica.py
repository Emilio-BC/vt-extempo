import matplotlib.pyplot as plt
import numpy as np

# Datos del Cuarteto de Anscombe
x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.0, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68] # Ajustado a los valores estándar para mayor precisión visual, que coinciden con los redondeos de tu tabla
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

datasets = [(x, y1, 'Dataset 1'), (x, y2, 'Dataset 2'), (x, y3, 'Dataset 3'), (x4, y4, 'Dataset 4')]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs = axs.flatten()

# Ecuación de la recta: y = 3 + 0.5x
x_line = np.linspace(3, 20, 100)
y_line = 3 + 0.5 * x_line

for i, (x_data, y_data, title) in enumerate(datasets):
    axs[i].scatter(x_data, y_data, color='blue', s=40, label='Datos')
    axs[i].plot(x_line, y_line, color='red', linestyle='--', label='Regresión')
    axs[i].set_title(title)
    axs[i].set_xlim(2, 20)
    axs[i].set_ylim(2, 14)
    axs[i].set_xlabel('X')
    axs[i].set_ylabel('Y')
    axs[i].grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()
