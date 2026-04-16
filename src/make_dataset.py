# Script de Preparación de Datos
###################################

import pandas as pd
import numpy as np
import os
import functions as fu
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler

model_features=["paginas",
                "valor",
                "edad",
                "nivel_usuario",
                "acciones_imput",
                "duracion_imput_4",
                "pais_Argentina",
                "pais_Chile",
                "pais_España",
                "pais_Mexico",
                "pais_USA",
                "experiencia_alta",
                "experiencia_baja",
                "experiencia_media",
                "navegador_Chrome",
                "navegador_Edge",
                "navegador_Firefox",
                "navegador_Safari",
                "hora_dia_imput_mañana",
                "hora_dia_imput_noche",
                "hora_dia_imput_tarde"]

# Leemos los archivos csv
def read_file_csv(filename):
    current_dir = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(current_dir,"..","data","raw", filename),encoding='latin1', sep = ';')
    print(filename, " cargado correctamente")
    return df

def data_preparation(data,type):

    numeric_vars = data.select_dtypes(include=['number']).columns.tolist()
    categorical_vars = data.select_dtypes(include=['object', 'category']).columns.tolist()

    data['acciones_imput'] = data['acciones']
    data = fu.imputar_valores_extremos(data, 'acciones_imput', metodo='mediana')
    data['acciones_imput'] = data['acciones']

    # Imputar valores extremos en la columna 'variable1' usando la media
    data = fu.imputar_valores_extremos(data, 'acciones_imput', metodo='mediana')

    numeric_vars.remove('acciones')
    numeric_vars.append('acciones_imput')

    data['hora_dia_imput'] = data['hora_dia']
    data = fu.imputar_valores(data,'hora_dia_imput',metodo='moda')

    categorical_vars.remove('hora_dia')
    categorical_vars.append('hora_dia_imput')

    data['duracion_imput'] = data['duracion'].fillna(data['duracion'].mean()) # Imputando los valores perdidos por la media
    data['duracion_imput_2'] = data['duracion'].fillna(data['duracion'].median()) # Imputando los valores perdidos por la mediana
    data['duracion_imput_3'] = data['duracion'].fillna(data['duracion'].mode()[0]) # Imputando los valores perdidos por la moda


    # Selección de variables para la imputación
    vars_imputacion = ['duracion', 'paginas', 'acciones_imput', 'nivel_usuario', 'valor']

    df_imputacion = data[vars_imputacion] # Filtrar solo las columnas necesarias
    imputer = IterativeImputer(random_state=42) # Crear el imputador con un modelo base (ejemplo: regresión bayesiana)

    # Aplicar la imputación
    df_imputado = imputer.fit_transform(df_imputacion)
    df_imputado = pd.DataFrame(df_imputado, columns=vars_imputacion)
    data['duracion_imput_4'] = df_imputado['duracion']

    numeric_vars.remove('duracion')
    numeric_vars.append('duracion_imput_4')

    if( type==0): 
        numeric_vars.remove('clase')
        label = data["clase"]

    cat_cols = data[categorical_vars]
    num_cols = data[numeric_vars]

    # Generar variables para las dos columnas que omiti de mi mapeo de variables cualitativas y cuantitativas
    cat_cols = pd.get_dummies(data = cat_cols) #transformamos las variables categóricas a numéricas
    
    if( type==1): 
        df_end = pd.concat([num_cols, cat_cols], axis=1).reindex(columns=model_features, fill_value=0)
        return df_end
    else :

        df_complete = pd.concat([num_cols, cat_cols, label], axis=1)
        #Elimina la columna clase (OS)
        X = df_complete.drop("clase",axis=1) # covariables

        y = df_complete['clase'] # target
        X_train_res, X_test, y_train_res, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

        oversampler = RandomOverSampler(random_state=42)
        X_train_over, y_train_over = oversampler.fit_resample(X_train_res, y_train_res)

        df_train = pd.concat([X_train_over, y_train_over], axis=1)
        df_test= pd.concat([X_test,y_test],axis=1)

        name_train= "data_train.csv"
        data_exporting(df_train,name_train)
        name_val="data_val.csv"
        data_exporting(df_test,name_val)

    
def data_exporting(df, filename):
    current_dir = os.path.dirname(__file__)
    df.to_csv(os.path.join(current_dir,"..","data","processed", filename))
    print(filename, "exportado correctamente en la carpeta processed")


def main():
    df = read_file_csv("usuarios_win_mac_lin_exp_cmp.csv")
    data_preparation(df,0)

if __name__ == "__main__":
    main()
