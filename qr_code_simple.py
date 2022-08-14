import qrcode

data = 'https://www.linkedin.com/in/wellingtonbarcelos'

img = qrcode.make(data)

img.save('C:/Users/vitor/OneDrive/Documentos/WELLINGTON/Programação/python/Projetos/código qr_code/myqrcode.png')
