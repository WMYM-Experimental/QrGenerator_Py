import qrcode
from PIL import Image

link = 'https://github.com/WashingtonYandun' #link, text or number . This is just an example
img = qrcode.make(link)

nameImg = 'gol.png'
fileImg = open(nameImg, 'wb')
img.save(fileImg)
fileImg.close()

ph = './'+ nameImg
img.open(ph).show()
