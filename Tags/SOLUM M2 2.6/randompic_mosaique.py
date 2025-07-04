import os, random

try:
    from PIL import Image
except:
    os.system('pip install pillow')
    from PIL import Image

mywidth = 639
myheight = 550

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

# Based on my random pic script, but stretched to height, not width.
# Made for a 6 Tag mosaique. Sizes made for Solum M2 2.6" Tags. The three
# on the right are turned by 180° to get rid of the barcode in the middle
# of the image. Borders are approximated with 25 Pixel size. Thus between
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
im_crop1.save('./frame_temp/tempframe1.jpg', quality=95)
im_crop2 = img.crop((343, 0, 639, 152))
im_crop2 = im_crop2.rotate(180)
im_crop2.save('./frame_temp/tempframe2.jpg', quality=95)
im_crop3 = img.crop((0, 199, 296, 351))
im_crop3.save('./frame_temp/tempframe3.jpg', quality=95)
im_crop4 = img.crop((343, 199, 639, 351))
im_crop4 = im_crop4.rotate(180)
im_crop4.save('./frame_temp/tempframe4.jpg', quality=95)
im_crop5 = img.crop((0, 398, 296, 550))
im_crop5.save('./frame_temp/tempframe5.jpg', quality=95)
im_crop6 = img.crop((343, 398, 639, 550))
im_crop6 = im_crop6.rotate(180)
im_crop6.save('./frame_temp/tempframe6.jpg', quality=95)

print (random_file)
