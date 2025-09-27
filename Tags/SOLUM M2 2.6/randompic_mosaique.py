import os, random, json

# Additional manual NSFW Blocker
nsfw = 1

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

# Size of the picture mosaique.
mywidth = 639
myheight = 550

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
if NSFWState == 'home' and nsfw == 0::
    folders = ['NSFW','Safe']
    selected_folder = random.choice(folders)
    print ("NSFW Mode active")
else:
    selected_folder = 'Safe'
    print ("Safe Mode active")

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

# Based on my random pic script.
# Made for a 6 Tag mosaique. Sizes made for Solum M2 2.6" Tags. The three
# on the right are turned by 180° to get rid of the barcode in the middle
# of the image. Borders are approximated with ~24 Pixel size. Thus between
# all the pics are always 47(,36) Pixels of nothingness due to the
# borders of the two Tags lying next to each other.

#------------------------------------------------------------------------
#- (0,0)                            -- (343,0)                          -
#-                                  --                                  -
#-                        (296,152) --                        (639,152) -
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#- (0,199)                          -- (343,199)                        -
#-                                  --                                  -
#-                        (296,351) --                        (639,351) -
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#- (0,398)                          -- (343,398)                        -
#-                                  --                                  -
#-                        (296,550) --                        (639,550) -
#------------------------------------------------------------------------

im_crop1 = img.crop((0, 0, 296, 152))
im_crop1.save('../frame_temp/tempframe1.jpg', quality=85)
im_crop2 = img.crop((343, 0, 639, 152))
im_crop2 = im_crop2.rotate(180)
im_crop2.save('../frame_temp/tempframe2.jpg', quality=85)
im_crop3 = img.crop((0, 199, 296, 351))
im_crop3.save('../frame_temp/tempframe3.jpg', quality=85)
im_crop4 = img.crop((343, 199, 639, 351))
im_crop4 = im_crop4.rotate(180)
im_crop4.save('../frame_temp/tempframe4.jpg', quality=85)
im_crop5 = img.crop((0, 398, 296, 550))
im_crop5.save('../frame_temp/tempframe5.jpg', quality=85)
im_crop6 = img.crop((343, 398, 639, 550))
im_crop6 = im_crop6.rotate(180)
im_crop6.save('../frame_temp/tempframe6.jpg', quality=85)

# Output for the shell_command used to run this script.
print (random_file)
