import qrcode
from PIL import Image 

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("https://github.com/shanna33?tab=overview&from=2026-09-01&to=2026-09-28")

qr.make(fit=True)
img=qr.make_image(fill_color="Red",back_color="Purple")
img.save("shanna_github_qr.png")

