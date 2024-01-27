import numpy

#inputs = [3, 1]
inputs = [-1, 4]
hidden_layer = [[6, -2], [-3, 5]]
layer_ans = [[1, 0.25], [-2, 2]]

# list_ans = [(1.75, 6.5), (1.5, 4.25), (6.25, 5.0), (2.0, 3.5), (1.0, 1.75), (7.75, 8.0), (1.75, 7.5), (7.75, 6.75), 
# 			(2.25, 9.0), (3.75, 9.25), (4.0, 3.0), (5.0, 0.75), (8.25, 7.75), (1.75, 2.0), (9.75, 5.5), (6.75, 6.0), 
# 			(6.0, 1.5), (2.75, 3.75), (0.75, 6.75), (0.25, 7.0), (2.25, 9.75), (4.0, 3.75), (5.5, 8.5), (2.75, 6.25), 
# 			(6.25, 2.5), (1.0, 5.0), (9.75, 0.5), (2.25, 1.5), (8.25, 5.25), (2.25, 5.0), (3.75, 4.0), (5.75, 10.0), 
# 			(7.75, 4.5), (9.0, 10.0), (3.75, 0.75), (6.0, 9.25), (9.25, 8.25), (1.5, 3.0), (5.75, 5.25), (7.0, 5.0), 
# 			(8.0, 5.5), (1.75, 8.5), (3.0, 3.0), (6.0, 3.75), (2.75, 6.25), (6.0, 1.75), (2.0, 10.0), (3.25, 7.0), 
# 			(7.75, 6.25), (6.5, 0.75)]

euler = numpy.exp(1)
sigmoid = lambda x: round(1/(1 + euler**(-x)), 4)

class Neural_func:
	def __init__(self, answer):
		self.answer = answer

	def layer_process(self, lay_1, weights):
		return [round(sigmoid(sum([ele_lay_1 * ele_wei[indx_lay_1] for indx_lay_1, ele_lay_1 in enumerate(lay_1)])), 4)
				for indx_wei, ele_wei in enumerate(weights)]

	def der_cost_func(self, lis):
		return [2*(i - 1) if indx == self.answer else 2*(i - 0) for indx, i in enumerate(lis)]

	def der_wei(self, layer, der_not_sigmoided):
		return [[round(i * e, 4) for e in layer] for i in der_not_sigmoided]

	def der_not_sigmoided(self, layer, der_sigmoided):
		return [round(i * (1 - i) * der_sigmoided[indx], 4) for indx, i in enumerate(layer)]

	def der_sigmoided(self, weights, der_not_sigmoided):
		return [round(sum([e * weights[indx_e][indx_i] for indx_e, e in enumerate(der_not_sigmoided)]), 4) for indx_i, i in enumerate(weights[0])]

Neural_func = Neural_func(1)

output_hidden_layer = Neural_func.layer_process(inputs, hidden_layer)
output_layer_ans = Neural_func.layer_process(output_hidden_layer, layer_ans)

print(f"Hidden Layer results: {output_hidden_layer}")
print(f"Answers: {output_layer_ans}")

der_sigmoided_ans = Neural_func.der_cost_func(output_layer_ans)
print(f"Gradients of sigmoided answer: {der_sigmoided_ans}")

der_not_sigmoided_ans = Neural_func.der_not_sigmoided(output_layer_ans, der_sigmoided_ans)
print(f"Gradients of not sigmoided answer: {der_not_sigmoided_ans}")

der_wei_2 = Neural_func.der_wei(output_hidden_layer, der_not_sigmoided_ans)
print(f"Gradients of the 2nd weights: {der_wei_2}")

der_hidden_layer_sigmoided = Neural_func.der_sigmoided(layer_ans, der_not_sigmoided_ans)
print(f"Gradients of sigmoided hidden layer: {der_hidden_layer_sigmoided}")

der_hidden_layer_not_sigmoided = Neural_func.der_not_sigmoided(output_hidden_layer, der_hidden_layer_sigmoided)
print(f"Gradients of not sigmoided hidden layer: {der_hidden_layer_not_sigmoided}")

der_wei_1 = Neural_func.der_wei(inputs, der_hidden_layer_not_sigmoided)
print(f"Gradients of the 1st weights: {der_wei_1}")

learning_func = lambda layer_1, slope_layer_1, learn_rate=0.05: [[round(layer_1[indx_i][indx_e] - (e * learn_rate), 4) for indx_e, e in enumerate(i)] for indx_i, i in enumerate(slope_layer_1)]
new_wei_1 = learning_func(hidden_layer, der_wei_1)
new_wei_ans = learning_func(layer_ans, der_wei_2) 

print(f'new weights for layer 1: {new_wei_1}') 
print(f'new weights for layer 2/ans: {new_wei_ans}') 

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
# 	#print(main_list)
# 	MainDataFile.write_seg(main_list)

# list_everything = json.loads(MainDataFile.read())

# lis_der_wei_1 = [runs[0][0] for runs in list_everything]
# lis_der_wei_2 = [runs[1][0] for runs in list_everything]
# lis_der_wei_ans = [runs[2][0] for runs in list_everything]

# print(list_get_avg(*lis_der_wei_ans))






	# def layer_process(self, lay_1, weights):
	# 	layer_output = []
	# 	for indx_wei, ele_wei in enumerate(weights):
	# 		total = 0
	# 		for indx_lay_1, ele_lay_1 in enumerate(lay_1):
	# 			total += ele_lay_1 * ele_wei[indx_lay_1]
	# 		layer_output.append(round(sigmoid(total), 4))
	# 	return layer_output