import qrcode

qr = qrcode.QRCode(
    version = 10, #Higher version means bigger code image, i.e., more complicated picture
    box_size = 10, #Size of the box where QR Code is displayed
    border = 5 #Thickness of the border 
)

data = "https://www.linkedin.com/in/sahilsr20/"
#Link/text data for which we generate the QR Code
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("QRCode.png")
