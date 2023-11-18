from flask import Flask, request
from laptopsService import *
app = Flask(__name__)

@app.route('/api/laptops', methods=['GET'])
def getLaptops():
    return getAllLaptops()

@app.route('/api/laptops/filter', methods=['GET'])
def filterLaptops():
    brand = request.args.get('brand')
    priceMin = request.args.get('priceMin')
    priceMax = request.args.get('priceMax')
    typeStorage = request.args.get('typeStorage')
    cpu = request.args.get('cpu')
    gpu = request.args.get('gpu')
    order = request.args.get('order')
    
    priceMin = float(priceMin) if priceMin != None else None
    priceMax = float(priceMax) if priceMax != None else None
    return filterAllLaptops(brand, priceMin, priceMax, cpu, gpu, typeStorage,order)

@app.route('/api/laptops/<int:id>', methods=['GET'])
def getLaptopById(id):
    return getLaptopByIdService(id)

@app.route('/api/laptops/<int:id>/recommendation', methods=['GET'])
def getRecommendations(id:int):
    return getRecommendationByLaptopId(id)  

@app.route('/api/laptops/search', methods=['GET'])
def getLaptopsByName():
    name = request.args.get('name')
    return searchByName(name)
 
@app.route('/api/laptops/<int:id>/recommendation/filter', methods=['GET'])
def getFilterRecommendations(id:int):
    brand = request.args.get('brand')
    status = request.args.get('status')
    price = request.args.get('price')
    typeStorage = request.args.get('typeStorage')
    cpu = request.args.get('cpu')
    gpu = request.args.get('gpu')
    storage = request.args.get('storage')
    
    brand = bool(brand) if brand != None else None
    status = bool(status) if status != None else None
    price = bool(price) if price != None else None
    typeStorage = bool(typeStorage) if typeStorage != None else None
    cpu = bool(cpu) if cpu != None else None
    gpu = bool(gpu) if gpu != None else None
    storage = bool(storage) if storage != None else None

    
    return filterRecommendations(id, brand, status, price, typeStorage, cpu, gpu, storage)

@app.route('/api/user/register', methods=['POST'])
def register():
    fullName = request.json.get('fullName')
    email = request.json.get('email')
    password = request.json.get('password')
    professionalTitle = request.json.get('professionalTitle')
    userRegister = {
        "fullName": fullName,
        "email": email,
        "password": password,
        "professionalTitle": professionalTitle
    }
    return registerService(userRegister)
@app.route('/api/user/login', methods=['GET'])
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    userLogin = {
        "email": email,
        "password": password,
    }
    return loginService(userLogin)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5000)