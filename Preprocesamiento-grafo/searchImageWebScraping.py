import requests
from bs4 import BeautifulSoup

def obtener_url_imagen_google_scraping(query):
    base_url = "https://www.google.com/search"
    
    # Define los parámetros de la solicitud
    params = {
        "q": query,
        "tbm": "isch",  # Modo de imágenes
    }

    # Realiza la solicitud a la página de resultados de búsqueda de Google Images
    response = requests.get("base_url", params=params)
    
    # Parsea la página con BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Encuentra la URL de la primera imagen (puedes ajustar esto según la estructura del sitio web)
    img_element = soup.find("img")
    if img_element:
        image_url = img_element["src"]
        return image_url
    else:
        return None

# Ejemplo de uso
nombre_laptop = "Asus Zenbook"
marca_laptop = " Asus"
query = f"{nombre_laptop} {marca_laptop} laptop"

# Obtiene la URL de la imagen
url_imagen = obtener_url_imagen_google_scraping(query)

# Imprime la URL de la imagen (puedes agregar esto a tu diccionario)
if url_imagen:
    print(f"URL de la imagen para {nombre_laptop}: {url_imagen}")
else:
    print(f"No se encontraron imágenes para {nombre_laptop}")
