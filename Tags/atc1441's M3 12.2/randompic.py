import os, random

try:
    from PIL import Image
except:
    os.system('pip install pillow')
    from PIL import Image

mywidth = 960
myheight = 768

os.chdir('./media/')
random_file=random.choice(os.listdir("."))

img = Image.open(random_file)

if img.size[0] > img.size[1]:
    wpercent = (myheight/float(img.size[1]))
    vsize = int((float(img.size[0])*float(wpercent)))
    img = img.resize((vsize,myheight),1)
else:
    wpercent = (mywidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((mywidth,hsize),1)

img = img.convert('RGB')
img.save('./frame_temp/tempframe.jpg', quality=95)

print (random_file)
