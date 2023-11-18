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

def similitud_global(laptop1, laptop2, _caracteristicas_numericas, _caracteristicas_de_texto):
    # Calcula una medida de similitud global entre dos laptops
    caracteristicas_numericas = _caracteristicas_numericas
    caracteristicas_de_texto = _caracteristicas_de_texto

    try:
        similitud_numerica = sum(similitud_euclidiana(laptop1[car], laptop2[car]) for car in caracteristicas_numericas)/len(caracteristicas_numericas)
    except:
        similitud_numerica = 0
        
    try:
        similitud_texto = sum(similitud_de_Levenshtein(laptop1[car], laptop2[car]) for car in caracteristicas_de_texto)/len(caracteristicas_de_texto)
    except:
        similitud_texto = 0

    similitud_total = (similitud_numerica + similitud_texto)/2 if len(caracteristicas_numericas) > 0 and len(caracteristicas_de_texto) > 0 else similitud_numerica if len(caracteristicas_numericas) > 0 else similitud_texto
    
    return similitud_total


def ponderarGrafo(_caracteristicas_numericas:[], _caracteristicas_de_texto:[]):
    nodeList = []
    with open("api\datos-laptos.json", "r") as archivo:
        nodeList = json.load(archivo)

# Calculamos la similitud entre cada par de laptops
    listAdj = {}
    listAdjNoPonderada = {}
#n = len(nodeList)
    n = 500
    identificador = "id"
    for i in range(n):
        adj = []
        for j in range(i + 1, n):
            similitud = similitud_global(nodeList[i], nodeList[j], _caracteristicas_numericas, _caracteristicas_de_texto)
            node1 = {nodeList[j][identificador]: round(similitud,2)}
            node2 = {nodeList[i][identificador]: round(similitud,2)}
        
            node1NoPonderado = nodeList[j][identificador]
            node2NoPonderado = nodeList[i][identificador]
            if similitud > 0.70:
                if nodeList[i][identificador] not in listAdj:
                    listAdj[nodeList[i][identificador]] = []
                    listAdjNoPonderada[nodeList[i][identificador]] = []
                if nodeList[j][identificador] not in listAdj:
                    listAdj[nodeList[j][identificador]] = []
                    listAdjNoPonderada[nodeList[j][identificador]] = []
                listAdj[nodeList[i][identificador]].append(node1)
                listAdj[nodeList[j][identificador]].append(node2)
                listAdjNoPonderada[nodeList[i][identificador]].append(node1NoPonderado)
                listAdjNoPonderada[nodeList[j][identificador]].append(node2NoPonderado)
            
    return listAdjNoPonderada