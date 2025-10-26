import pyqrcode,os,png
link='https://www.jetbrains.com/pycharm/'
image=pyqrcode.create(link)
image.png('link.png',scale=10)
os.system('start link.png')
