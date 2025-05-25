"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
def load_data(file):
    return pd.read_csv(file, sep='\t')
def tabla_c0_lista_c4(df):
    # Agrupa por c0 y concatena los valores únicos de c4 ordenados y separados por ','
    return df.groupby('c0')['c4'].apply(lambda x: ','.join(sorted(set(x)))).reset_index()

def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    # Lee el archivo tbl1.tsv
    df = load_data("files/input/tbl1.tsv")
    # Devuelve una tabla que contenga c0 y una lista separada por ',' de los valores de la columna c4
    return tabla_c0_lista_c4(df)

#test
if __name__ == "__main__":
    print(pregunta_11())
    # Output:
    #      c0       c4
    # 0     0    b,f,g
    # 1     1    a,c,f
    # 2     2  a,c,e,f
    # 3     3      a,b
    # ...
    # 37   37  a,c,e,f
    # 38   38      d,e
    # 39   39    a,d,f