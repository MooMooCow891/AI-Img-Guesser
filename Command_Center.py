import os
import shutil
import random
from datetime import datetime
import sys
import json
from Main_AI_Part import input_list, layer_1, layer_2, layer_ans, wei_1, wei_2, wei_answer, layer_1_neuron, layer_2_neuron, layer_answer_neuron
#sys.path.insert(1, "C:\\Users\\Lenovo\\Tony\\Code\\Program for Statistic\\edit_file.py")
from edit_file import EditFile
from avg_ele_list import list_get_avg

img_path = None
result = None
number_3s_path = None
bees_path = None
img_of_3s_list = None
img_of_bees_list = None


def pick_ran():
	global img_path, result, number_3s_path, bees_path, img_of_3s_list, img_of_bees_list

	number_3s_path = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Original Source\\3"
	bees_path = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Original Source\\Bee"

	img_of_3s_list = [i for i in os.listdir(number_3s_path) if os.path.isfile(number_3s_path + "\\" + i)]
	img_of_bees_list = [i for i in os.listdir(bees_path) if os.path.isfile(bees_path + "\\" + i)]
	result = random.choice([1, 2])

	with open("C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\img_path.txt", "w") as write_img_path:
		if result == 1:
			try:
				img_path = '"' + number_3s_path + "\\" + str(img_of_3s_list[random.choice([i for i in range(len(img_of_3s_list))])]) + '"'
				write_img_path.write(img_path)
			except:
				try:
					img_path = '"' + bees_path + "\\" + str(img_of_bees_list[random.choice([i for i in range(len(img_of_bees_list))])]) + '"'
					write_img_path.write(img_path)
					result = 2
				except:
					exit("All data exhausted. Training's done.")
		else:
			try:
				img_path = '"' + bees_path + "\\" + str(img_of_bees_list[random.choice([i for i in range(len(img_of_bees_list))])]) + '"'
				write_img_path.write(img_path)
			except:
				try:
					img_path = '"' + number_3s_path + "\\" + str(img_of_3s_list[random.choice([i for i in range(len(img_of_3s_list))])]) + '"'
					write_img_path.write(img_path)
					result = 1
				except:
					exit("All data exhausted. Training's done.")

	print("Result = {}".format(result))
	print(f"Image path: {img_path}")

	return result

def move_to_trash_bin():
	if result == 1:
		print("Chosen: 3")
		shutil.move(img_path[1:-1], number_3s_path + "\\Used") #remove quotation marks

	if result == 2: 
		print("Chosen: Bee")
		shutil.move(img_path[1:-1], bees_path + "\\Used") #remove quotation marks


# learning_func = lambda layer_1, slope_layer_1, learn_rate=0.05: [[round(layer_1[indx_i][indx_e] - (e * learn_rate), 4) for indx_e, e in enumerate(i)] for indx_i, i in enumerate(slope_layer_1)]
# new_wei_1 = learning_func(wei_1, der_wei_1)
# new_wei_2 = learning_func(wei_2, der_wei_2)  
# new_wei_answer = learning_func(wei_answer, der_wei_ans) 

# with open(layer_1_neuron, "w") as new_layer_1:
# 	new_layer_1.write(str(new_wei_1))

# with open(layer_2_neuron, "w") as new_layer_2:
# 	new_layer_2.write(str(new_wei_2))

# with open(layer_answer_neuron, "w") as new_layer_ans:
# 	new_layer_ans.write(str(new_wei_answer))

# ----------------------------------------------------------
# <!-- Create new backup -->

def backup():
	date = "{} {}".format(get_month_day()[0], get_month_day()[1]) 
	path_list_of_layer = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Neural Network"
	path_neu_net_backup = f"C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Neural Network - Backup\\{date}, 2024\\Neural Program Backups"
	
	if os.path.exists(f"C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Neural Network - Backup\\{date}, 2024") == False:
		os.mkdir(f"C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Neural Network - Backup\\{date}, 2024")

	if os.path.exists(f"C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Neural Network - Backup\\{date}, 2024\\Neural Program Backups") == False:
		os.mkdir(f"C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Neural Network - Backup\\{date}, 2024\\Neural Program Backups")

	dir_list_of_layers = os.listdir(path_list_of_layer)
	dir_neu_net_backup = sorted([int(i) for i in os.listdir(path_neu_net_backup)])

	new_save = 1 if len(dir_neu_net_backup) == 0 else dir_neu_net_backup[-1] + 1
	os.mkdir(path_neu_net_backup + "\\" + str(new_save))

	for i in dir_list_of_layers:
		# shutil.copy(path_list_of_layer + "\\" + i, path_neu_net_backup + "\\" + str(new_save) + "\\" + i)
		shutil.copy(f"{path_list_of_layer}\\{i}", f"{path_neu_net_backup}\\{new_save}\\{i}")

def get_month_day():
	today = datetime.now()
	number = [i for i in range(1, 13)]
	name = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
	dictionary = dict(zip(number, name))
	return dictionary[today.month], today.day
# ------------------------------------------------------------------

# while True:
# 	MainDataFile = EditFile("main_data_file.txt", anew=True)
# 	DataFile = EditFile("data.txt", anew=False)

# 	for i in range(1474 + 1474 + 1):
# 		if i == 0:
# 			MainDataFile.write_seg("[]")

# 		print("------ Command Center choosing and processing --------")
# 		pick_ran()
# 		print("------ Command Center ended ------\n")
# 		print("------ Processing Image running --------")
# 		os.system("python Process_Img.py")
# 		print("------ Processing Image ended ----\n")	
# 		print("------ AI Learning Mode running --------")
# 		os.system("python AI_Learning_Part.py")
# 		print("------ AI Learning Mode ended ------\n")

# 		print("------ Save training result --------")
# 		list_data = json.loads(DataFile.read())
# 		main_list = json.loads(MainDataFile.read())
# 		MainDataFile.clear()
# 		main_list.append(list_data)
# 		MainDataFile.write_seg(main_list)
# 		print("------ Saving ended --------")

# 		print("------ Command Center cleaning --------")
# 		move_to_trash_bin()
# 		print("------ Command Center ended ------\n")

# 	print("------ Average Training Process --------")
# 	list_everything = json.loads(MainDataFile.read())

# 	lis_new_wei_1 = [runs[0] for runs in list_everything]
# 	lis_new_wei_2 = [runs[1] for runs in list_everything]
# 	lis_new_wei_ans = [runs[2] for runs in list_everything]

# 	print(f"{lis_new_wei_ans} <-- lis_new_wei_ans")
# 	MainDataFile.clear()
# 	MainDataFile.write(runs[2])
# 	exit()

# 	new_wei_1 = list_get_avg(*lis_new_wei_1)
# 	new_wei_2 = list_get_avg(*lis_new_wei_2)
# 	new_wei_ans = list_get_avg(*lis_new_wei_ans)

# 	with open(layer_1_neuron, "w") as new_layer_1:
# 		new_layer_1.write(str(new_wei_1))

# 	with open(layer_2_neuron, "w") as new_layer_2:
# 		new_layer_2.write(str(new_wei_2))

# 	with open(layer_answer_neuron, "w") as new_layer_ans:
# 		new_layer_ans.write(str(new_wei_ans))

# 	print("------ Average Training Process Ended --------")

# 	print("------ Command Center saving --------")
# 	backup()
# 	print("------ Command Center ended ------\n")	

while True:
	for i in range(1474 + 1474 + 1):
		print("------ Command Center choosing and processing --------")
		pick_ran()
		print("------ Command Center ended ------\n")
		print("------ Processing Image running --------")
		os.system("python Process_Img.py")
		print("------ Processing Image ended ----\n")	
		print("------ AI Learning Mode running --------")
		os.system("python AI_Learning_Part.py")
		print("------ AI Learning Mode ended ------\n")

		print("------ Save training result --------")
		DataFile = EditFile("data.txt", anew=False)
		Layer1File = EditFile(layer_1_neuron, anew=True)
		Layer2File = EditFile(layer_2_neuron, anew=True)
		LayerAnswerFile = EditFile(layer_answer_neuron, anew=True)
		
		list_data = json.loads(DataFile.read())
		Layer1File.write_seg(list_data[0])
		Layer2File.write_seg(list_data[1])
		LayerAnswerFile.write_seg(list_data[2])
		print("------ Saving ended --------")

		print("------ Command Center cleaning --------")
		move_to_trash_bin()
		print("------ Command Center ended ------\n")

		print("------ Command Center saving --------")
		backup()
		print("------ Command Center ended ------\n")

# for i in range(10):
# 	print("------ Command Center choosing and processing --------")
# 	pick_ran()
# 	print("------ Command Center ended ------\n")
# 	print("------ Processing Image running --------")
# 	os.system("python Process_Img.py")
# 	print("------ Processing Image ended ----\n")	

# 	print("------ AI Learning Mode running --------")
# 	os.system("python AI_Learning_Part.py")
# 	print("------ AI Learning Mode ended ------\n")	

# with open("C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\der_wei_ans.csv", "r") as read_gradients:
# 	saved_gradients.write(",".join([str(i) for i in der_wei_ans]) + "\n")


# with open("C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\der_wei_ans.txt", "w") as read_gradients:
# 	saved_gradients.write(",".join([str(i) for i in der_wei_ans]) + "\n")


# print("------ Command Center cleaning --------")
# move_to_trash_bin()
# print("------ Command Center ended ------\n")
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

# MainDataFile = EditFile("main_data_file.txt", anew=True)
# DataFile = EditFile("data.txt", anew=False)
# times = 5
# for i in range(times):
# 	if i == 0:
# 		MainDataFile.write_seg("[]")

# 	list_data = json.loads(DataFile.read())
# 	main_list = json.loads(MainDataFile.read())
# 	MainDataFile.clear()
# 	main_list.append(list_data)
# 	MainDataFile.write_seg(main_list)

# list_everything = json.loads(MainDataFile.read())

# lis_new_wei_1 = [runs[0][0] for runs in list_everything]
# lis_new_wei_2 = [runs[1][0] for runs in list_everything]
# lis_new_wei_ans = [runs[2][0] for runs in list_everything]

# print(list_get_avg(*lis_new_wei_ans))
