import math
import Levenshtein
import json
def similitud_euclidiana(a:float, b:float):
    # Calcula la distancia euclidiana entre dos  números
    similitud = 1 / (1 + abs(a - b))
    return similitud
    
def similitud_de_Levenshtein(a:str, b:str):
    if(a == "" or b == ""):
        return 0
    similitud = 1 - (Levenshtein.distance(a, b) / max(len(a), len(b)))
    return similitud

def similitud_global(laptop1, laptop2):
    # Calcula una medida de similitud global entre dos laptops
    caracteristicas_numericas = ["RAM", "Storage", "Screen", "Final Price"]
    caracteristicas_de_texto = ["Laptop", "Brand", "Model", "CPU", "Storage type", "GPU", "Touch"]

    similitud_numerica = sum(similitud_euclidiana(laptop1[car], laptop2[car]) for car in caracteristicas_numericas)/len(caracteristicas_numericas)
    similitud_texto = sum(similitud_de_Levenshtein(laptop1[car], laptop2[car]) for car in caracteristicas_de_texto)/len(caracteristicas_de_texto)

    print("Similitud numerica: ", similitud_numerica)
    print("Similitud de texto: ", similitud_texto)
    print()
    similitud_total = (similitud_numerica + similitud_texto)/2
    return similitud_total

nodeList = []
with open("Preprocesamiento-grafo/datos-laptos.json", "r") as archivo:
    nodeList = json.load(archivo)

# Calculamos la similitud entre cada par de laptops
listAdj = {}
listAdjNoPonderada = {}
#n = len(nodeList)
n = 200
for i in range(n):
    adj = []
    for j in range(i + 1, n):
        similitud = similitud_global(nodeList[i], nodeList[j])
        node1 = {nodeList[j]['Laptop']: round(similitud,2)}
        node2 = {nodeList[i]['Laptop']: round(similitud,2)}
        
        node1NoPonderado = nodeList[j]['Laptop']
        node2NoPonderado = nodeList[i]['Laptop']
        if similitud > 0.70:
            if nodeList[i]['Laptop'] not in listAdj:
                listAdj[nodeList[i]['Laptop']] = []
                listAdjNoPonderada[nodeList[i]['Laptop']] = []
            if nodeList[j]['Laptop'] not in listAdj:
                listAdj[nodeList[j]['Laptop']] = []
                listAdjNoPonderada[nodeList[j]['Laptop']] = []
            listAdj[nodeList[i]['Laptop']].append(node1)
            listAdj[nodeList[j]['Laptop']].append(node2)
            listAdjNoPonderada[nodeList[i]['Laptop']].append(node1NoPonderado)
            listAdjNoPonderada[nodeList[j]['Laptop']].append(node2NoPonderado)
            
with open("lista-adyacencia.json", "w") as archivo:
    json.dump(listAdj, archivo)

with open("lista-adyacencia-no-ponderada.json", "w") as archivo:
    json.dump(listAdjNoPonderada, archivo)
    