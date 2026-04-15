# Función imputación de outlier
# ------
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def imputar_valores_extremos(df, variable, metodo='media'):
    """
    Imputa valores extremos en una variable de un DataFrame utilizando la media o la mediana.

    Parámetros:
    df (DataFrame): El DataFrame que contiene la variable a imputar.
    variable (str): El nombre de la variable que deseas imputar.
    metodo (str): La forma de imputación ('media' o 'mediana'). Por defecto es 'media'.

    Retorna:
    DataFrame: El DataFrame con la variable imputada.
    """
    if metodo not in ['media', 'mediana']:
        raise ValueError("El método debe ser 'media' o 'mediana'")

    # Calcular la media o la mediana
    if metodo == 'media':
        valor_imputacion = df[variable].mean()
    else:
        valor_imputacion = df[variable].median()

    # Identificar valores extremos (usando una regla de 3 veces la desviación estándar)
    limite_inferior = df[variable].mean() - 1.9 * df[variable].std()
    limite_superior = df[variable].mean() + 1.9 * df[variable].std()

    # Imputar valores extremos
    df[variable] = np.where(
        (df[variable] < limite_inferior) | (df[variable] > limite_superior),
        valor_imputacion,
        df[variable]
    )

    return df


# Función imputación perdidos
# ------

def imputar_valores(df, variable, metodo='media', valor_especifico=None):
    """
    Imputa valores perdidos en una columna de un DataFrame según el método especificado.

    Parámetros:
    df (pd.DataFrame): El DataFrame en el que se imputarán los valores.
    variable (str): El nombre de la columna a imputar.
    metodo (str): El método de imputación ('media', 'mediana', 'moda', 'valor_especifico').
    valor_especifico: El valor específico a usar para la imputación (relevante solo si 'metodo' es 'valor_especifico').

    Retorna:
    pd.DataFrame: El DataFrame con la variable imputada.
    """

    if metodo == 'media':
        imputacion = df[variable].mean()
    elif metodo == 'mediana':
        imputacion = df[variable].median()
    elif metodo == 'moda':
        imputacion = df[variable].mode()[0]
    elif metodo == 'valor_especifico':
        if valor_especifico is None:
            raise ValueError("Debe proporcionar un valor específico para la imputación.")
        imputacion = valor_especifico
    else:
        raise ValueError("Método de imputación no reconocido. Use 'media', 'mediana', 'moda' o 'valor_especifico'.")

    df[variable].fillna(imputacion, inplace=True)
    return df


def calcular_valores_perdidos(df):
    """
    Calcula la cantidad y el porcentaje de valores NaN en cada variable del DataFrame.

    Parámetros:
    df (pd.DataFrame): DataFrame con las variables a analizar.

    Retorna:
    pd.DataFrame: Un DataFrame con el resumen de valores perdidos, mostrando:
        - Variable: Nombre de la columna analizada.
        - Total: Cantidad total de filas en la variable.
        - Valores Perdidos: Cantidad de valores NaN en la variable.
        - % Valores Perdidos: Porcentaje de valores NaN respecto al total (con 2 decimales).
    """
    resumen_perdidos = []  # Lista para almacenar los resultados

    for col in df.columns:  # Analizar todas las columnas
        total = df[col].shape[0]  # Total de filas en la columna
        valores_perdidos = df[col].isna().sum()  # Conteo de valores NaN

        # Calcular el porcentaje de valores perdidos
        porcentaje_perdidos = (valores_perdidos / total) * 100 if total > 0 else 0

        # Agregar la información a la lista de resultados
        resumen_perdidos.append([col, total, valores_perdidos, f"{porcentaje_perdidos:.2f}%"])

    # Convertir la lista en un DataFrame
    df_resumen = pd.DataFrame(resumen_perdidos, columns=['Variable', 'Total', 'Valores Perdidos', '% Valores Perdidos'])

    return df_resumen



# Funcion graficadora confusion_marix
# ---
def confusion_matrix_graph(cm):
  plt.figure(figsize=(8, 6))
  sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
              xticklabels=['No', 'Yes'],
              yticklabels=['No', 'Yes'])
  plt.title('Matriz de Confusión')
  plt.xlabel('Predicción')
  plt.ylabel('Realidad')
  plt.show()


  # Función para detectar valores atípicos con el método IQR
def detectar_outliers(df):
    resumen = {}
    for col in df.select_dtypes(include=['number']):  # Solo columnas numéricas
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        porcentaje_outliers = (len(outliers) / len(df)) * 100

        resumen[col] = f"{porcentaje_outliers:.1f}% ({len(outliers)} valores atípicos)"

    return resumen
