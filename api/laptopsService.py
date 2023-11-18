import json
import sys
from Dfs import *
from Ponderacion import *
with open ('api\datos-laptos.json', 'r') as f:
        data = json.load(f)
        
with open ('api\list-ady-general.json', 'r') as f:
        ady = json.load(f)


def getAllLaptops():
    return data

def filterAllLaptops(brand:str = None, priceMin:float=None, priceMax:float=None, cpu: str=None, gpu:str=None, typeStorage:str=None, order:str=None):
    response = []
    cadena = ""
    for laptop in data:
        matchBrand = brand == None or brand.upper() in laptop['Brand'].upper()
        matchPriceMin = priceMin == None or laptop["Final Price"] >= priceMin
        matchPriceMax = priceMax == None or laptop["Final Price"] <= priceMax
        matchCpu = cpu == None or cpu.upper() in laptop['CPU'].upper()
        matchGpu = gpu == None or gpu.upper() in laptop['GPU'].upper()
        matchTypeStorage = typeStorage == None or typeStorage.upper() in laptop['Storage type'].upper()
        
        if matchBrand and matchPriceMin and matchPriceMax and matchCpu and matchGpu and matchTypeStorage:
            response.append(laptop)
    if(order == None):
        order = "ASC"
    if(order == "ASC"):
        response = sorted(response, key=lambda k: k['Final Price'])
    elif(order == "DESC"):
        response = sorted(response, key=lambda k: k['Final Price'], reverse=True)
    return response

def getLaptopByIdService(id):
    return data[id-1] if id > 0 and id <= len(data) else None

def getRecommendationByLaptopId(id:int):
    recommendations = ApplyDFS(str(id))
    response = []
    for recommendation in recommendations:
        response.append(data[int(recommendation)-1])
    return response

def searchByName(name:str):
    if(name == None):
        return []
    response = []
    for laptop in data:
        if name.upper() in laptop['Laptop'].upper():
            response.append(laptop)
    return response

def filterRecommendations(id:int,brand:bool = None, status:bool = None, price:bool=None, typeStorage:bool=None, cpu:bool=None, gpu:bool=None, storage:bool=None):
    caracteristicas_numericas = []
    caracteristicas_de_texto = []
    if(brand == True):
        caracteristicas_de_texto.append("Brand")
    if(status == True):
        caracteristicas_de_texto.append("Status")
    if(price == True):
        caracteristicas_numericas.append("Final Price")
    if(typeStorage == True):
        caracteristicas_de_texto.append("Storage type")
    if(cpu == True):
        caracteristicas_de_texto.append("CPU")
    if(gpu == True):
        caracteristicas_de_texto.append("GPU")
    if(storage == True):
        caracteristicas_numericas.append("Storage")
    
    nombreListaAdyacencia = ""
    for car in caracteristicas_numericas:
        nombreListaAdyacencia += car + "-"
    for car in caracteristicas_de_texto:
        nombreListaAdyacencia += car + "-"
    nombreListaAdyacencia = nombreListaAdyacencia[:-1]
    nombreListaAdyacencia += ".json"
    
    listAdj = {}
    
    if(len(caracteristicas_numericas) == 0 and len(caracteristicas_de_texto) == 0):
        listAdj = ady
    else:
        try:
            with open("api\list-ady-" + nombreListaAdyacencia, "r") as archivo:
                listAdj = json.load(archivo)
        except:
            
            listAdj = ponderarGrafo(caracteristicas_numericas, caracteristicas_de_texto)
            with open("api\list-ady-"+nombreListaAdyacencia, "w") as archivo:
                json.dump(listAdj, archivo)
            with open("api\list-ady-" + nombreListaAdyacencia, "r") as archivo:
                listAdj = json.load(archivo)

    recommendations =  ApplyDFS(str(id), listAdj)
    print("Recomendaciones: ", recommendations)
    response = []
    for recommendation in recommendations:
        response.append(data[int(recommendation)-1])
    return response

def registerService(userRegister:{}):
    data = []
    try:
        with open("api/users.json", "r") as archivo:
            data = json.load(archivo)
    except:
        with open("api/users.json", "w") as archivo:
            json.dump(data, archivo)
    userRegister['id'] = len(data) + 1
    data.append(userRegister)
    with open("api/users.json", "w") as archivo:
        json.dump(data, archivo)
    return {"register": "success"}
        
def loginService(userLogin:{}):
    data = []
    response = {}
    try:
        with open("api/users.json", "r") as archivo:
            data = json.load(archivo)
    except:
        with open("api/users.json", "w") as archivo:
            json.dump(data, archivo)
    for user in data:
        if(user['email'] == userLogin['email'] and user['password'] == userLogin['password']):
            response["permission"] = True
            return response
    response["permission"] = False
    return response