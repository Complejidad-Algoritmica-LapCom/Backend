import pandas as pd 
import json
from searchImages import getUrlImage

df = pd.read_csv("laptops.csv")
df = df.fillna("")
laptops = []
id_laptop = 1
for index, row in df.iterrows():
    fila_diccionario = {"id": id_laptop}
    for columna in df.columns:
        fila_diccionario[columna] = row[columna]
    fila_diccionario = {"urlImage": getUrlImage(fila_diccionario["Brand"],fila_diccionario["Model"])} 
    laptops.append(fila_diccionario)
    id_laptop += 1
    
with open("datos-laptos.json", "w") as archivo:
    json.dump(laptops, archivo)
