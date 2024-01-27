from Main_AI_Part import input_list, layer_1, layer_2, layer_ans, wei_1, wei_2, wei_answer, layer_1_neuron, layer_2_neuron, layer_answer_neuron
from Process_Img import img_path
import numpy
import os
import shutil
import json
from edit_file import EditFile

with open("img_path.txt", "r") as read_img_path:
	answer = 0 if "\\Original Source\\3\\" in read_img_path.read() else 1

#print(f"Path = {read_img_path.read()}")
#print(f'Answer = {"3" if answer == 0 else "Bee"}')

euler = numpy.exp(1)
error_slope = lambda lis: [2*(i - 1) if indx == answer else 2*(i - 0) for indx, i in enumerate(lis)]
sigmoided_der = lambda sigmoided_func: round(sigmoided_func * (1 - sigmoided_func), 2)

#print("<!-- This is before the weights get adjusted -->")
#print(f"3: {layer_ans[0]}, bee: {layer_ans[1]}")

class Neural_func:
	def __init__(self, answer):
		self.answer = answer

	def der_cost_func(self, lis):
		return [2*(i - 1) if indx == self.answer else 2*(i - 0) for indx, i in enumerate(lis)]

	def der_wei(self, layer, der_not_sigmoided):
		return [[round(i * e, 4) for e in layer] for i in der_not_sigmoided]

	def der_not_sigmoided(self, layer, der_sigmoided):
		return [round(i * (1 - i) * der_sigmoided[indx], 4) for indx, i in enumerate(layer)]

	def der_sigmoided(self, weights, der_not_sigmoided):
		return [round(sum([e * weights[indx_e][indx_i] for indx_e, e in enumerate(der_not_sigmoided)]), 4) for indx_i, i in enumerate(weights[0])]

Neural_func = Neural_func(answer)

der_sigmoided_ans = Neural_func.der_cost_func(layer_ans)

der_not_sigmoided_ans = Neural_func.der_not_sigmoided(layer_ans, der_sigmoided_ans)

der_wei_ans = Neural_func.der_wei(layer_2, der_not_sigmoided_ans)

der_layer_2_sigmoided = Neural_func.der_sigmoided(wei_answer, der_not_sigmoided_ans)

der_layer_2_not_sigmoided = Neural_func.der_not_sigmoided(layer_2, der_layer_2_sigmoided)

der_wei_2 = Neural_func.der_wei(layer_1, der_layer_2_not_sigmoided)

der_layer_1_sigmoided = Neural_func.der_sigmoided(wei_2, der_layer_2_not_sigmoided)

der_layer_1_not_sigmoided = Neural_func.der_not_sigmoided(layer_2, der_layer_1_sigmoided)

der_wei_1 = Neural_func.der_wei(input_list, der_layer_1_not_sigmoided)


# with open("C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Training Results\\der_wei_ans.csv", "a") as saved_gradients:
# 	saved_gradients.write(",".join([str(i) for i in der_wei_ans]) + "\n")

with open("C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Training Results\\wei_ans.csv", "a") as saved_wei_ans:
	saved_wei_ans.write(",".join([str(i) for i in wei_answer]) + "\n")

# print(f"derivitive of weight_answer: {der_wei_ans}")
# print(f"weight_answer: {wei_answer}")

learning_func = lambda layer_1, slope_layer_1, learn_rate=0.05: [[round(layer_1[indx_i][indx_e] - (e * learn_rate), 4) for indx_e, e in enumerate(i)] for indx_i, i in enumerate(slope_layer_1)]
new_wei_1 = learning_func(wei_1, der_wei_1)
new_wei_2 = learning_func(wei_2, der_wei_2)  
new_wei_answer = learning_func(wei_answer, der_wei_ans)

DataFile = EditFile("data.txt", anew=True)
DataFile.write_seg(f"{[new_wei_1, new_wei_2, new_wei_answer]}")
# test_1, test_2, test_not_ans = json.loads(DataFile.read())

# wei_ans_list = []
# with open("C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Training Results\\wei_ans.csv", "r") as read_saved_wei_ans:
# 	while True:	
# 		wei_ans_str = read_saved_wei_ans.readline()

# 		if wei_ans_str != "":
# 			wei_ans_list.append(wei_ans_str.split(","))
# 		else:
# 			break

# process_list = lambda lis: [[int(e.strip()) if float(e.strip()) % 1 == 0 else float(e.strip()) for e in i] for i in lis]
# def get_list(path):
# 	result = []
# 	with open(path, "r") as name:
# 		while True:
# 			line = name.readline()

# 			if line != "":
# 				result.append(line.split(","))
# 			else:
# 				return process_list(result)
# 				break

# wei_ans_list = get_list("C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Training Results\\wei_ans.csv")


# print(wei_ans_list)

# with open("C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\der_wei_ans.csv", "w") as saved_gradients:
# 	pass