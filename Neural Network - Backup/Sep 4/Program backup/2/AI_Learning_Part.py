from Main_AI_Part import input_list, layer_1, layer_2, layer_ans, wei_1, wei_2, wei_answer, layer_1_neuron, layer_2_neuron, layer_answer_neuron
from Process_Img import img_path
import numpy
import os 
import shutil

def get_month_day():
	today = datetime.now()
	number = [i for i in range(1, 13)]
	name = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
	dictionary = dict(zip(number, name))
	return dictionary[today.month], today.day

with open("img_path.txt", "r") as read_img_path:
	answer = 0 if "\\Original Source\\3\\" in read_img_path.read() else 1

print(f"Path = {read_img_path.read()}")
print(f'Answer = {"3" if answer == 0 else "Bee"}')

euler = numpy.exp(1)
error_slope = lambda lis: [2*(i - 1) if indx == answer else 2*(i - 0) for indx, i in enumerate(lis)]
sigmoided_der = lambda sigmoided_func: round(sigmoided_func * (1 - sigmoided_func), 2)

print(f"3: {layer_ans[0]}, bee: {layer_ans[1]}")

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

learning_func = lambda layer_1, slope_layer_1, learn_rate: [[round(layer_1[indx_i][indx_e] - (e * learn_rate), 4) for indx_e, e in enumerate(i)] for indx_i, i in enumerate(slope_layer_1)]
learning_rate = 0.1
new_wei_1 = learning_func(wei_1, der_wei_1, learning_rate)
new_wei_2 = learning_func(wei_2, der_wei_2, learning_rate)  
new_wei_answer = learning_func(wei_answer, der_wei_ans, learning_rate) 

with open(layer_1_neuron, "w") as new_layer_1:
	new_layer_1.write(str(new_wei_1))

with open(layer_2_neuron, "w") as new_layer_2:
	new_layer_2.write(str(new_wei_2))

with open(layer_answer_neuron, "w") as new_layer_ans:
	new_layer_ans.write(str(new_wei_answer))
