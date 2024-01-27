import numpy
import json
from Process_Img import list_data_of_img
from random import *

data = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Image Data\\List of a bunch of data.txt"
layer_1_neuron = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Neural Network\\Nerons Layer 1.txt"
layer_2_neuron = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Neural Network\\Nerons Layer 2.txt"
layer_answer_neuron = "C:\\Users\\Lenovo\\Tony\\Code\\AI Img guesser test\\Neural Network\\Nerons Layer Answer.txt"
list_of_ans = ["3", "bee"]
euler = numpy.exp(1)
greyscale_binary = lambda x: round(x/255, 2)
sigmoid = lambda x: round(1/(1 + euler**(-x)), 2)

with open(data, "r") as read_data_file:
	#print([round(greyscale_binary(int(i))) for i in json.loads(data_file.read())])
	input_list = [greyscale_binary(i) for i in json.loads(read_data_file.read())]


with open(layer_1_neuron, "r") as read_hidden_layer_1:
	#write_hidden_layer_1.writelines(str([[randrange(-100, 101)/100 for i in input_list] + [randrange(-10, 11)] for e in range(20)]))
	wei_n_bias_1 = json.loads(read_hidden_layer_1.read())


with open(layer_2_neuron, "r") as read_hidden_layer_2:
	#write_hidden_layer_2.writelines(str([[randrange(-100, 101)/100 for i in wei_n_bias_1] + [randrange(-10, 11)] for e in range(20)]))
	wei_n_bias_2 = json.loads(read_hidden_layer_2.read())

with open(layer_answer_neuron, "r") as read_layer_answer_neuron:
	#write_layer_answer_neuron.writelines(str([[randrange(-100, 101)/100 for i in wei_n_bias_2] + [randrange(-10, 11)] for e in range(2)]))
	wei_n_bias_answer = json.loads(read_layer_answer_neuron.read())

# <!-- broken here??? -->
def layer_process(lay_1, wei_n_bias):
	layer_output = []
	for indx_wei_n_bias, ele_wei_n_bias in enumerate(wei_n_bias):
		total = 0
		for indx_lay_1, ele_lay_1 in enumerate(lay_1):
			total += round(ele_lay_1 * ele_wei_n_bias[indx_lay_1], 2)

		layer_output.append(round(sigmoid(total + ele_wei_n_bias[-1]), 2))

	return layer_output
# <!-- /broken here??? -->

# layer_1 = [sigmoid(round(sum(round(ele_input * ele_lay_1[indx_input], 2) for indx_input, ele_input in enumerate(input_list)) + ele_lay_1[-1], 2)) for indx_lay_1, ele_lay_1 in enumerate(wei_n_bias_1)]
layer_1 = layer_process(input_list, wei_n_bias_1)
layer_2 = layer_process(layer_1, wei_n_bias_2)
layer_ans = layer_process(layer_2, wei_n_bias_answer)

print(layer_1)
print(layer_2)
print(layer_ans)

#print(len(wei_n_bias_1))

#error_cost = lambda dic: round(sum([round((value - 1)**2, 2) if key == "3" else round((value - 0)**2, 2) for key, value in dic.items()]), 2)
#print("Error Cost: " + str(error_cost(layer_ans)))



