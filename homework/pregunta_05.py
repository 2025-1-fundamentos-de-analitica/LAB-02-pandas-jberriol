"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
def load_data(file):
    return pd.read_csv(file, sep='\t')

def valor_maximo_c2_por_cada_letra_columna_c1(df):
    return df.groupby('c1')['c2'].max()


def pregunta_05():
    """
    Calcule el valor máximo de `c2` por cada letra en la columna `c1` del
    archivo `tbl0.tsv`.

    Rta/
    c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: c2, dtype: int64
    """
    # Lee el archivo tbl0.tsv
    df = load_data("files/input/tbl0.tsv")
    # Devuelve el valor máximo de c2 por cada letra de la c1
    return valor_maximo_c2_por_cada_letra_columna_c1(df)