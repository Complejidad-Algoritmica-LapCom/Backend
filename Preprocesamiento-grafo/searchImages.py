import requests

def obtener_url_imagen_google_api(query, api_key):
    base_url = "https://www.googleapis.com/customsearch/v1"
    cx = "02d0e22225a924625"  # Reemplaza con tu CX

    params = {
        "q": query,
        "cx": cx,
        "key": api_key,
        "searchType": "image",
        "num": 1,
    }

    try:
        response = requests.get(base_url, params=params)
        json_response = response.json()
        if "items" in json_response and len(json_response["items"]) > 0:
            image_url = json_response["items"][0]["link"]
            return image_url
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Ejemplo de uso con clave de API

def getUrlImage(marca,modelo):
    # Ejemplo de uso

    query = f"{marca} {modelo} laptop"

    # Obtiene la URL de la imagen
    api_key = "AIzaSyALd6ZhnGXx8S-gkNp3SKCeWV-WzhBxNgQ"
    url_imagen = obtener_url_imagen_google_api(query, api_key)

    # Imprime la URL de la imagen (puedes agregar esto a tu diccionario)
    if url_imagen:
        print(f"URL de la imagen para {marca} {modelo}: {url_imagen}")
    else:
        print(f"No se encontraron imágenes para {marca} {modelo}")
