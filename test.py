import requests
from PIL import Image, ImageTk
import io

def display_image(category):
    # make a request to the Unsplash API to get a random image
    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=1n7sSMtCh8Hs_MrBOjhQ1SygTDA-BJ550UdX3rwLYZQ"
    data = requests.get(url).json()
    img_data = requests.get(data["urls"]["regular"]).content

    photo = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)).resize((600, 400), resample=Image.LANCZOS))

display_image('create horse')