# import qrcode
# from PIL import Image

# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=10,
#     border=4,
# )
# qr.add_data('https://www.youtube.com/watch?v=UfFb_Af4kiw')
# qr.make(fit=True)

# img = qr.make_image(fill_color="Red", back_color="white")
# img.save("youtubecustom.png")
import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myyoutube.jpg", scale = 8) 