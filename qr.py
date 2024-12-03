import qrcode

img = qrcode.make("https//youtu.be/xvFZj05PgG0")
img.save("qr.png", "PNG")
