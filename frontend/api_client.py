import requests

BASE_URL = "https://astronomical-image-archive-1.onrender.com"

def search_images(params):
    response=requests.get(f"{BASE_URL}/search",params=params)
    response.raise_for_status()
    return response.json()

def get_image_details(image_id):
    response=requests.get(f"{BASE_URL}/images/{image_id}")
    response.raise_for_status()
    return response.json()

def upload_image(file):
    files={"file":(file.name,file.getvalue())}
    response=requests.post(f"{BASE_URL}/upload",files=files)
    return response

def get_thumbnail_url(image_id):
    return f"{BASE_URL}/images/{image_id}/thumbnail"

def get_file_url(image_id):
    return f"{BASE_URL}/images/{image_id}/file"
