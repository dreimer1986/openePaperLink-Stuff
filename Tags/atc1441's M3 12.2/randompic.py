import os, random, json

try:
    from PIL import Image
except:
    os.system('pip install pillow')
    from PIL import Image

try:
    from requests import get
except:
    os.system('pip install requests')
    from requests import get

mywidth = 960
myheight = 768

url = 'http://homeassistant.local:8123/api/states/device_tracker.pixel_7_pro'
headers = {
    'Authorization': 'Bearer ---',
    'content-type': 'application/json'
}

NSFWVar = get(url, headers=headers)
NSFWData = json.loads(NSFWVar.text)
NSFWState = NSFWData["state"]

if NSFWState == 'home':
    folders = ['NSFW','Safe']
    selected_folder = random.choice(folders)
else:
    selected_folder = 'Safe'

os.chdir('./media/' + selected_folder)
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
img.save('../frame_temp/tempframe.jpg', quality=85)

print (random_file)
