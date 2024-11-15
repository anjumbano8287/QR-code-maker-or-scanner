import qrcode as qr
img=qr.make("https://www.geeksforgeeks.org/")
img.save("geekssitescanner.png")
print("Your QR code is successfully created")