"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
def load_data(file):
    return pd.read_csv(file, sep='\t')

def registros_por_cada_letra_columna_c1(df):
    return df.groupby('c1').size()


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
    # Lee el archivo tbl0.tsv
    df = load_data("files/input/tbl0.tsv")
    # Devuelve la cantidad de registros por cada letra de la columna c1
    return registros_por_cada_letra_columna_c1(df)
