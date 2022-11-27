from io import BytesIO

from PIL import Image

from sphinx.util import requests

profil = requests.get('https://pbs.twimg.com/profile_images/1367965835617132544/mS8gW7MV_normal.jpg')
img = Image.open(BytesIO(profil.content))

