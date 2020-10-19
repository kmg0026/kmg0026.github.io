import pyqrcode
import png
from pyqrcode import QRCode


s = "https://kmg0026.github.io/"

url = pyqrcode.create(s)

url.svg('myqr.svg', scale = 8)

url.png('myqr.png', scale = 6)
