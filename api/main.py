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
    
    priceMin = float(priceMin) if priceMin != None else None
    priceMax = float(priceMax) if priceMax != None else None
    return filterAllLaptops(brand, priceMin, priceMax, cpu, gpu, typeStorage)

@app.route('/api/laptops/<int:id>', methods=['GET'])
def getLaptopById(id:int):
    return getLaptopById(id)

@app.route('/api/laptops/<int:id>/recommendation', methods=['GET'])
def getRecommendations(id:int):
    return getRecommendationByLaptopId(id)  
 
if __name__ == '__main__':
    app.run(debug=True)