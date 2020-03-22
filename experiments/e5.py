from PIL import Image

im = Image.open('../Data/phone.jpeg')
im.show()

basewidth = 2000
img = Image.open('../Data/phone.jpeg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.show('../Data/phone.jpeg') 
