from PIL import Image

from os import listdir
from os.path import isfile, join
import sys

def combine(file1, file2):
	
	print(file1)
	print(file2)

	im1 = Image.open(file1)
	im2 = Image.open(file2)

	if im1.width < im1.height:
		im1 = im1.rotate(90, expand = 1)

	if im2.width < im2.height:
		im2 = im2.rotate(90, expand = 1)

	new_img_width = 0

	if im1.width > im2.width:
		new_img_width = im1.width
	else:
		new_img_width = im2.width

	new_img_height = im1.height + im2.height



	new_im = Image.new('RGB', (new_img_width,new_img_height))

	new_im.paste(im1, (0,0))

	new_im.paste(im2, (0, im1.height))

	new_im.save(mypath + "/" + str(i) + "merged.jpg")

mypath = sys.argv[1]

files = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f)) and (f.endswith(".jpg") or f.endswith(".JPG"))]

for i in range(0, len(files) - 1, 2):
	combine(files[i], files[i + 1])