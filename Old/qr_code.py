import pyqrcode
import png
from pyqrcode import QRCode


s = "https://iithelp.vetmed.auburn.edu/kris/static/index.html"

url = pyqrcode.create(s)

url.svg('myqr.svg', scale = 8)

url.png('myqr.png', scale = 6)
