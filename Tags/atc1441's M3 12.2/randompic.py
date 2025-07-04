import os, random

try:
    from PIL import Image
except:
    os.system('pip install pillow')
    from PIL import Image

mywidth = 960

os.chdir('./media/')
random_file=random.choice(os.listdir("."))

img = Image.open(random_file)
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize),1)
img = img.convert('RGB')
img.save('./frame_temp/tempframe.jpg', quality=95)

print (random_file)