from PIL import Image
import os
import shutil


with open("img_path.txt", "r") as file:
	img_path = file.read()[1:-1]

new_img_path = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Greyscaled Source\\new_img.png"
list_data_of_img = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Image Data\\List of a bunch of data.txt"
#matrix_data_of_img = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Image Data\\Matrix of a bunch of data.txt"

img = Image.open(img_path)

img = img.resize((50, 50), Image.ANTIALIAS).convert('L')

folder_path = 'C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Greyscaled Source'
shutil.rmtree(folder_path)
os.mkdir(folder_path)

img.save(new_img_path)

list_pixels = list(img.getdata())
length_list_pixels = len(list_pixels)

with open(list_data_of_img, "w") as data_list:
	data_list.write(str(list_pixels))

""" 
<!-- Unnecessary Stuff -->

matrix_pixels = [list_pixels[i * 50 : (i + 1)*50] for i in range(int(length_list_pixels/50))] 
data_matrix = open(matrix_data_of_img, "w")
data_matrix.write(str(matrix_pixels))
"""

"""
<!-- Reconstructing image -->
reconstruct = Image.new('RGB', (50, 50), color='white')
for y, lis in enumerate(matrix_pixels):
	for x, ele in enumerate(lis):
		reconstruct.putpixel((x, y), (ele, ele, ele))

reconstruct.save('new_image.jpg')
"""