import pyqrcode 
import png 
from pyqrcode import QRCode 


user_input = raw_input("Enter web page address or info you want to convert into qr code: ")
user_input = pyqrcode.create(user_input) 
user_input.png('myqr.png', scale = 6) 
