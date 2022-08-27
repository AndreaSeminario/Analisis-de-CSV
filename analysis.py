# Para analisis de datos (pandas // package)
import pandas
# Para graficar (matplotlib // package)
#              (pyplot// module)
# import matplotlib.pyplot as plt

# Para leer .csv
tabla = pandas.read_csv('registro_mipyme_09-05-2022.csv')

# Conteo por sector
print(tabla['Sector'].value_counts())
print(tabla['Sector'].value_counts(normalize=True))  # %

# Conteo por Provincia
print(tabla['Provincia'].value_counts())
print(tabla['Provincia'].value_counts(normalize=True))  # %

# Conteo por Regimen Tributario
print(tabla['Regimen_Tributario'].value_counts())
print(tabla['Regimen_Tributario'].value_counts(normalize=True))  # %

# Conteo por Categoria
print(tabla['Categoria'].value_counts())
print(tabla['Categoria'].value_counts(normalize=True))  # %
