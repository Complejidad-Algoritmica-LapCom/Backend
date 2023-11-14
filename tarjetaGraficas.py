import json
nodeList = []
with open("Preprocesamiento-grafo/datos-laptos.json", "r") as archivo:
    nodeList = json.load(archivo)

tarjetasGraficas = set()
marcas = set()
for laptop in nodeList:
    if(laptop['GPU'] == ""):
        continue
    tarjetasGraficas.add(laptop['GPU'])
    
for laptop in nodeList:
    marcas.add(laptop['Brand'])
    
with open("Preprocesamiento-grafo/tarjetas-graficas.json", "w") as archivo:
    json.dump(list(tarjetasGraficas), archivo)
with open("Preprocesamiento-grafo/marcas.json", "w") as archivo:
    json.dump(list(marcas), archivo)