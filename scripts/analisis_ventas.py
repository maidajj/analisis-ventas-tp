
import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv("../datos/ventas.csv")

# Ventas totales
ventas_totales = df["amount"].sum()

# Procesamiento de fechas
df["sales_date"] = pd.to_datetime(df["sales_date"])
df["mes"] = df["sales_date"].dt.month

# Ventas por mes
ventas_mes = df.groupby("mes")["amount"].sum()

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print(ventas_mes)

# Guardar resumen
with open("../resultados/resumen.txt", "w") as f:
    f.write(f"Ventas totales: {ventas_totales}\n")
    f.write(str(ventas_mes))

# Generar gráfico
ventas_mes.plot(kind="bar")

plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Ventas")

plt.savefig("../resultados/grafico_ventas.png")
plt.close()
