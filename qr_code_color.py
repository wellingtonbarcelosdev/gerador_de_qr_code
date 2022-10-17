from textwrap import fill
import qrcode
link = 'https://github.com/wellingtonbarcelosdev'
qr = qrcode.QRCode(version = 1, box_size = 10, border=5)
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('C:/Users/vitor/OneDrive/Documentos/WELLINGTON/Programação/python/Projetos/código qr_code/myqrcode1.png')
