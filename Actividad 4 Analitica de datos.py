import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración visual
sns.set_theme(style="whitegrid")

# Carga del dataset
import os

os.chdir(r"d:\Programacion")

df = pd.read_csv("Restaurantes_y_Domicilios_20260912.csv")

# ==========================================================
# INFORMACIÓN BÁSICA
# ==========================================================

print("Cantidad de registros:", len(df))
print("Cantidad de columnas:", len(df.columns))

print("\nTipos de dato y nulos:")
df.info()

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nPrimeros registros:")
print(df.head())


# ==========================================================
# CREACIÓN DE VARIABLES
# ==========================================================

# Longitud del nombre comercial
df["longitud_nombre"] = df["NOMBRE"].astype(str).str.len()

# Convertir teléfono a texto
df["TELEFONO"] = df["TELEFONO"].astype(str)

# Obtener los primeros tres dígitos del teléfono
df["prefijo_tel"] = df["TELEFONO"].str[:3]


# ==========================================================
# 1. MATPLOTLIB - BARRAS VERTICALES
# ==========================================================

conteo_ciiu = df["CIIU-1"].value_counts()

plt.figure(figsize=(8,5))

plt.bar(
    conteo_ciiu.index,
    conteo_ciiu.values,
    color="steelblue"
)

plt.title("Establecimientos por tipo de actividad (CIIU-1)")
plt.xlabel("Categoría")
plt.ylabel("Cantidad")

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()
plt.show()


# ==========================================================
# 2. MATPLOTLIB - BARRAS HORIZONTALES
# ==========================================================

top_ciiu4 = (
    df["CIIU-4"]
    .astype(str)
    .str.strip()
    .str.upper()
    .value_counts()
    .head(10)
)

plt.figure(figsize=(8,5))

plt.barh(
    top_ciiu4.index[::-1],
    top_ciiu4.values[::-1],
    color="darkorange"
)

plt.title("Top 10 descripciones de actividad más comunes")
plt.xlabel("Cantidad")
plt.ylabel("Actividad CIIU-4")

plt.tight_layout()
plt.show()


# ==========================================================
# 3. MATPLOTLIB - GRÁFICO DE PASTEL
# ==========================================================

plt.figure(figsize=(6,6))

plt.pie(
    conteo_ciiu.values,
    labels=conteo_ciiu.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Distribución proporcional por tipo de actividad")

plt.tight_layout()
plt.show()


# ==========================================================
# 4. MATPLOTLIB - HISTOGRAMA
# ==========================================================

plt.figure(figsize=(8,5))

plt.hist(
    df["longitud_nombre"],
    bins=15,
    color="seagreen",
    edgecolor="black"
)

plt.title("Distribución de la longitud del nombre comercial")
plt.xlabel("N° de caracteres")
plt.ylabel("Frecuencia")

plt.tight_layout()
plt.show()


# ==========================================================
# 5. MATPLOTLIB - GRÁFICO DE LÍNEA
# ==========================================================

top_prefijos = (
    df["prefijo_tel"]
    .value_counts()
    .head(10)
    .sort_index()
)

plt.figure(figsize=(8,5))

plt.plot(
    top_prefijos.index,
    top_prefijos.values,
    marker="o",
    color="crimson"
)

plt.title("Frecuencia por prefijo telefónico (Top 10)")
plt.xlabel("Prefijo telefónico")
plt.ylabel("Cantidad de establecimientos")

plt.tight_layout()
plt.show()


# ==========================================================
# 6. SEABORN - COUNTPLOT
# ==========================================================

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    y="CIIU-1",
    order=df["CIIU-1"].value_counts().index
)

plt.title("Conteo de establecimientos por categoría")
plt.xlabel("Cantidad")
plt.ylabel("Categoría CIIU-1")

plt.tight_layout()
plt.show()


# ==========================================================
# 7. SEABORN - BOXPLOT
# ==========================================================

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="CIIU-1",
    y="longitud_nombre"
)

plt.title("Longitud del nombre comercial según tipo de actividad")
plt.xlabel("Categoría CIIU-1")
plt.ylabel("Longitud del nombre")

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()
plt.show()


# ==========================================================
# 8. SEABORN - HISTPLOT + KDE
# ==========================================================

plt.figure(figsize=(8,5))

sns.histplot(
    data=df,
    x="longitud_nombre",
    kde=True
)

plt.title("Distribución de longitud del nombre con densidad")
plt.xlabel("Número de caracteres")
plt.ylabel("Frecuencia")

plt.tight_layout()
plt.show()


# ==========================================================
# 9. SEABORN - VIOLINPLOT
# ==========================================================

plt.figure(figsize=(8,5))

sns.violinplot(
    data=df,
    x="CIIU-1",
    y="longitud_nombre"
)

plt.title("Distribución de longitud del nombre por categoría")
plt.xlabel("Categoría CIIU-1")
plt.ylabel("Longitud del nombre")

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()
plt.show()


# ==========================================================
# 10. SEABORN - HEATMAP
# ==========================================================

top8 = (
    df["prefijo_tel"]
    .value_counts()
    .head(8)
    .index
)

df_top8 = df[
    df["prefijo_tel"].isin(top8)
]

tabla_cruzada = pd.crosstab(
    df_top8["prefijo_tel"],
    df_top8["CIIU-1"]
)

plt.figure(figsize=(9,6))

sns.heatmap(
    tabla_cruzada,
    annot=True,
    fmt="d",
    cmap="YlOrRd"
)

plt.title("Relación entre prefijo telefónico y tipo de actividad")
plt.xlabel("Tipo de actividad CIIU-1")
plt.ylabel("Prefijo telefónico")

plt.tight_layout()
plt.show()