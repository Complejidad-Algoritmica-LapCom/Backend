import pandas as pd 
import json

df = pd.read_csv("laptops.csv")
df = df.fillna("")
laptops = []
for index, row in df.iterrows():
    fila_diccionario = {}
    for columna in df.columns:
        fila_diccionario[columna] = row[columna]
            
    laptops.append(fila_diccionario)
with open("datos-laptos.json", "w") as archivo:
    json.dump(laptops, archivo)
