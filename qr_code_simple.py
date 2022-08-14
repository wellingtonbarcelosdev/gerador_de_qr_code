import qrcode

data = 'Don\'t forget to subscribe'

img = qrcode.make(data)

img.save('C:/Users/vitor/OneDrive/Documentos/WELLINGTON/Programação/python/Projetos/código qr_code/myqrcode.png')
