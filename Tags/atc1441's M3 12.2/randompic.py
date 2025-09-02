import os, random, json

# These scripts use some stuff that might be missing after every update of Home Assistant.
# So if it's missing, reinstall it, bypassing errors and a not working script...
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

# The script works in the folder "./config/media" and two subdirectories.
# If these are missing, create them and bypass errors and a not working script...
if not os.path.exists('./media'):
    os.makedirs('./media')
if not os.path.exists('./media/NSFW'):
    os.makedirs('./media/NSFW')
if not os.path.exists('./media/Safe'):
    os.makedirs('./media/Safe')
if not os.path.exists('./media/frame_temp'):
    os.makedirs('./media/frame_temp')

# Size of the picture frame.
mywidth = 960
myheight = 768

# Get the value of the device tracker from Home Assistant.
# These are the API URL and the Token for authentification.
url = 'http://homeassistant.local:8123/api/states/device_tracker.pixel_7_pro'
headers = {
    'Authorization': 'Bearer ---',
    'content-type': 'application/json'
}

# Get the real tracker state value out of the JSON data inside a string.
NSFWVar = get(url, headers=headers)
NSFWData = json.loads(NSFWVar.text)
NSFWState = NSFWData["state"]

# Pr0n or not, that's the question ^^
# And by random choose the folder to use if pr0n is fine.
if NSFWState == 'home':
    folders = ['NSFW','Safe']
    selected_folder = random.choice(folders)
else:
    selected_folder = 'Safe'

# Hop into the folder, choose a random image and open it.
os.chdir('./media/' + selected_folder)
random_file=random.choice(os.listdir("."))
img = Image.open(random_file)

# Choose the best way to resize the image keeping most of the pic intact
# and still don't allow white borders
if img.size[0] > img.size[1]:
    wpercent = (myheight/float(img.size[1]))
    vsize = int((float(img.size[0])*float(wpercent)))
    img = img.resize((vsize,myheight),1)
else:
    wpercent = (mywidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((mywidth,hsize),1)

# FIX! If the input is a PNG file the file might be have different color
# encoding which is not allowed for JPG files.
img = img.convert('RGB')

# Save the file for the automation to work with it.
img.save('../frame_temp/tempframe.jpg', quality=85)

# Output for the shell_command used to run this script.
print (random_file)
