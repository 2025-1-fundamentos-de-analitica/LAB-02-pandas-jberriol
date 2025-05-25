"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
def load_data(file):
    return pd.read_csv(file, sep='\t')

def lista_unicos_columna_c4(df):
    return df['c4'].unique()

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    # Lee el archivo tbl1.tsv
    df = load_data("files/input/tbl1.tsv")
    # Devuelve una lista con los valores unicos de la columna c4 en mayusculas y ordenados alfabéticamente
    return sorted([str(x).upper() for x in lista_unicos_columna_c4(df)])


