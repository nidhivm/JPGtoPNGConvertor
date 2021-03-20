import sys
import os
from PIL import Image, ImageFilter
from pathlib import Path

# use sys to grab the two arguments 
image_folder  = sys.argv[1]  #folder containing jpg images
output_folder = sys.argv[2]  #new folder name with png images

#check if new/ folder exists, if not then create
if not os.path.exists(output_folder):
	os.makedirs(output_folder)  # create new folder

#loop through Pokedox
#convert images to PNG 
#save to new folder 
for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0] #gives you a tuple with name and extention
	img.save(f'{output_folder}{clean_name}.png', 'png')
	print('all done!')
    


