"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
def load_data(file):
    return pd.read_csv(file, sep='\t')
def tabla_c0_lista_c5a_c5b(df):
    df["c5"] = df["c5a"] + ":" + df["c5b"].astype(str)
    del df["c5a"]
    del df["c5b"]

    return df.groupby("c0")["c5"].apply(lambda x: ",".join(sorted(x)))

def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.

    Rta/
         c0                                   c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    df = load_data("files/input/tbl2.tsv")
    return tabla_c0_lista_c5a_c5b(df).reset_index()

#test
if __name__ == "__main__":
    print(pregunta_12())
    # Output:
    #      c0                                   c5
    # 0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    # 1     1              aaa:3,ccc:2,ddd:0,hhh:9
    # 2     2              ccc:6,ddd:2,ggg:5,jjj:1
    # ...
    # 37   37                    eee:0,fff:2,hhh:6
    # 38   38                    eee:0,fff:9,iii:2
    # 39   39                    ggg:3,hhh:8,jjj:5