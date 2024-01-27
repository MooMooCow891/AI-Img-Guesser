import os
import shutil

path_list_of_layer = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Neural Network"
path_neu_net_backup = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Neural Network - Backup\\August 9" + "\\Neural Network Backups"
# <!-- Time needs to be updated daily -->

dir_list_of_layers = os.listdir(path_list_of_layer)
dir_neu_net_backup = sorted([int(i) for i in os.listdir(path_neu_net_backup)])

new_save = dir_neu_net_backup[-1] + 1
os.mkdir(path_neu_net_backup + "\\" + str(new_save))

for i in dir_list_of_layers:
	shutil.copy(path_list_of_layer + "\\" + i, path_neu_net_backup + "\\" + str(new_save) + "\\" + i)