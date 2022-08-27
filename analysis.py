# Para analisis de datos (pandas // package)
import pandas
# Para graficar (matplotlib // package)
#              (pyplot// module)

import matplotlib.pyplot as plt

# Para leer .csv
tabla = pandas.read_csv(
    'C:\\Users\\Andre\\Documents\\INTI\\ProyectoPy\\registro_mipyme_09-05-2022.csv')

# Conteo por sector
print(tabla['Sector'].value_counts())
print(tabla['Sector'].value_counts(normalize=True))  # %
# Grafico sector
tabla['Sector'].value_counts().plot(kind="bar")
plt.show()

# Conteo por Provincia
print(tabla['Provincia'].value_counts())
print(tabla['Provincia'].value_counts(normalize=True))  # %
# Grafico Provincia
tabla['Provincia'].value_counts().plot(kind="bar")
plt.show()

# Conteo por Regimen Tributario
print(tabla['Regimen_Tributario'].value_counts())
print(tabla['Regimen_Tributario'].value_counts(normalize=True))  # %
# Grafico Regimen Tributario
tabla['Regimen_Tributario'].value_counts().plot(kind="bar")
plt.show()

# Conteo por Categoria
print(tabla['Categoria'].value_counts())
print(tabla['Categoria'].value_counts(normalize=True))  # %
# Grafico Categoria
tabla['Categoria'].value_counts().plot(kind="bar")
plt.show()
