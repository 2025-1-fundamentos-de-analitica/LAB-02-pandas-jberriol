"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
def load_data(file):
    return pd.read_csv(file, sep='\t')

def computar_suma_por_c1(df0, df2):
    # Combina los DataFrames en base a la columna c0
    merged_df = pd.merge(df0, df2, on='c0')
    # Agrupa por c1 y calcula la suma de c5b
    return merged_df.groupby('c1')['c5b'].sum()

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    # Lee los archivos tbl0.tsv y tbl2.tsv
    df0 = load_data("files/input/tbl0.tsv")
    df2 = load_data("files/input/tbl2.tsv")
    # Devuelve la suma de c5b por cada letra de la c1
    return computar_suma_por_c1(df0, df2)
