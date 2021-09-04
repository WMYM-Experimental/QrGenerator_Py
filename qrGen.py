import qrcode
from PIL import Image

link = 'https://github.com/WashingtonYandun' #link, text or number . This is just an example
imagen = qrcode.make(link)

nombreImagen = 'gol.png'
archivoImagen = open(nombreImagen, 'wb')
imagen.save(archivoImagen)
archivoImagen.close()

ruta = './'+nombreImagen
Image.open(ruta).show()
