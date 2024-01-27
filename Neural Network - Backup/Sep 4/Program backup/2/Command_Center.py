import os
import shutil
import random
from datetime import datetime

img_path = None
result = None

def pick_ran():
	global img_path, result
	number_3s_path = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Original Source\\3"
	bees_path = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Original Source\\Bee"

	img_of_3s_list = [i for i in os.listdir(number_3s_path) if os.path.isfile(number_3s_path + "\\" + i)]
	img_of_bees_list = [i for i in os.listdir(bees_path) if os.path.isfile(bees_path + "\\" + i)]
	result = random.choice([1, 2])

	test_read = open("C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\img_path.txt", "r")
	with open("C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\img_path.txt", "w") as write_img_path:
		if result == 1:
			try:
				img_path = '"' + number_3s_path + "\\" + str(img_of_3s_list[0]) + '"'
				write_img_path.write(img_path)
			except:
				try:
					img_path = '"' + bees_path + "\\" + str(img_of_bees_list[0]) + '"'
					write_img_path.write(img_path)
					result = 2
				except:
					exit("All data exhausted. Training done.")
		else:
			try:
				img_path = '"' + bees_path + "\\" + str(img_of_bees_list[0]) + '"'
				write_img_path.write(img_path)
			except:
				try:
					img_path = '"' + number_3s_path + "\\" + str(img_of_3s_list[0]) + '"'
					write_img_path.write(img_path)
					result = 1
				except:
					exit("All data exhausted. Training done.")

	print("Result = {}".format(result))

	return result

def move_to_trash_bin():
	if result == 1:
		print("Chosen: 3")
		shutil.move(img_path[1:-1], number_3s_path + "\\Used") #remove quotation marks

	if result == 2: 
		print("Chosen: Bee")
		shutil.move(img_path[1:-1], bees_path + "\\Used") #remove quotation marks
# ----------------------------------------------------------
# <!-- Create new backup -->

def backup():
	date = "{} {}".format(get_month_day()[0], get_month_day()[1]) 
	path_list_of_layer = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Neural Network"
	path_neu_net_backup = f"C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Neural Network - Backup\\{date}\\Neural Program Backups"
	# <!-- Time needs to be updated daily -->

	dir_list_of_layers = os.listdir(path_list_of_layer)
	dir_neu_net_backup = sorted([int(i) for i in os.listdir(path_neu_net_backup)])

	new_save = 1 if len(dir_neu_net_backup) == 0 else dir_neu_net_backup[-1] + 1
	os.mkdir(path_neu_net_backup + "\\" + str(new_save))

	for i in dir_list_of_layers:
		shutil.copy(path_list_of_layer + "\\" + i, path_neu_net_backup + "\\" + str(new_save) + "\\" + i)
# ------------------------------------------------------------------

while True:
	print("------ Command Center choosing and processing --------")
	pick_ran()
	print("------ Command Center ended ------\n")
	print("------ Processing Image running --------")
	os.system("python Process_Img.py")
	print("------ Processing Image ended ----\n")
	print("------ Command Center cleaning --------")
	move_to_trash_bin()
	print("------ Command Center ended ------\n")	
	print("------ AI Learning Mode running --------")
	os.system("python python AI_Learning_Part.py")
	print("------ AI Learning Mode ended ------\n")	
	print("------ Command Center saving --------")
	backup()
	print("------ Command Center ended ------\n")	

"""
with open("C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\img_path.txt", "w") as write_test:
	write_test.write(img_path)

with open("C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\img_path.txt", "r") as checking:
	print(checking.read())
"""

"""
os.system("python Process_Img.py")
os.system("python Main_AI_Part.py")
os.system("python AI_Learning_Part.py")
os.system("python Main_AI_Part.py")
"""