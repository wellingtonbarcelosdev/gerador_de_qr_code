import qrcode
link = 'https://www.linkedin.com/in/wellingtonbarcelos'
img = qrcode.make(link)
img.save('C:/Users/vitor/OneDrive/Documentos/WELLINGTON/Programação/python/Projetos/código qr_code/myqrcode.png')
