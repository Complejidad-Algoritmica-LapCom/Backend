import json
import sys
from Dfs import *

with open ('api\datos-laptos.json', 'r') as f:
        data = json.load(f)
with open ('api\lista-adyacencia-no-ponderada.json', 'r') as f:
        ady = json.load(f)


def getAllLaptops():
    return data

def filterAllLaptops(brand:str = None, priceMin:float=None, priceMax:float=None, cpu: str=None, gpu:str=None, typeStorage:str=None):
    response = []
    cadena = ""
    for laptop in data:
        matchBrand = brand == None or brand.upper() in laptop['Brand'].upper()
        matchPriceMin = priceMin == None or laptop['Price'] >= priceMin
        matchPriceMax = priceMax == None or laptop['Price'] <= priceMax
        matchCpu = cpu == None or cpu.upper() in laptop['CPU'].upper()
        matchGpu = gpu == None or gpu.upper() in laptop['GPU'].upper()
        matchTypeStorage = typeStorage == None or typeStorage.upper() in laptop['Storage type'].upper()
        if matchBrand and matchPriceMin and matchPriceMax and matchCpu and matchGpu:
            response.append(laptop)
    return response

def getLaptopById(id):
    for laptop in data:
        if laptop['id'] == id:
            return laptop
    return None    

def getRecommendationByLaptopId(id:int):
    recommendations = ApplyDFS(str(id),15)
    print(recommendations)
    response = []
    for recommendation in recommendations:
        response.append(data[int(recommendation)-1])
    return response

