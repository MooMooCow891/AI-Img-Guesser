from Main_AI_Part import input_list, layer_1, layer_2, layer_ans, wei_n_bias_1, wei_n_bias_2, wei_n_bias_answer, layer_1_neuron, layer_2_neuron, layer_answer_neuron
import numpy

answer = 0

euler = numpy.exp(1)
error_slope = lambda lis: [2*(i - 1) if indx == answer else 2*(i - 0) for indx, i in enumerate(lis)]
sigmoided_der = lambda sigmoided_func: round(sigmoided_func * (1 - sigmoided_func), 2)

print("3: " + str(layer_ans[0]) + ", bee: " + str(layer_ans[1]))

slope_of_error = error_slope(layer_ans)
print("Error Cost slope = " + "3: " + str(slope_of_error[0]) + ", bee: " + str(slope_of_error[1]))

slope_layer_ans = [sigmoided_der(i)*slope_of_error[indx] for indx, i in enumerate(layer_ans)]
print("slope layer ans = " + "3: " + str(slope_layer_ans[0]) + ", bee: " + str(slope_layer_ans[1]))

slope_wei_n_bias_answer = [[round(i * e, 4) for e in layer_2] for i in slope_layer_ans]
"""
for indx, i in enumerate(wei_n_bias_answer):
	for e in i:
		if indx == 0:
			round(e * slope_layer_ans["3"], 3) #round to the thousandth
		else:
			round(e * slope_layer_ans["bee"], 3) #round to the thousandth
"""
print("slope_wei_n_bias_answer = " + str(slope_wei_n_bias_answer))

slope_layer_2_sigmoided = [round(sum([e * wei_n_bias_answer[indx_e][indx_i] for indx_e, e in enumerate(slope_layer_ans)]), 3) for indx_i, i in enumerate(wei_n_bias_answer[0][:-1])]
print("slope_layer_2_sigmoided = " + str(slope_layer_2_sigmoided))

slope_layer_2_not_sigmoided = [round(sigmoided_der(i) * slope_layer_2_sigmoided[indx], 3) for indx, i in enumerate(layer_2)]
print("slope layer 2 not sigmoided = " + str(slope_layer_2_not_sigmoided))

slope_wei_n_bias_2 = [[round(e * i, 4) for e in layer_1] for i in slope_layer_2_not_sigmoided]
print("slope_wei_n_bias_2 = " + str(slope_wei_n_bias_2))

slope_layer_1_sigmoided = [round(sum([e * wei_n_bias_2[indx_2][indx_1] for indx_2, e in enumerate(slope_layer_2_not_sigmoided)]), 3) for indx_1, i in enumerate(wei_n_bias_2[0][:-1])]
print("slope_layer_1_sigmoided = " + str(slope_layer_1_sigmoided))

slope_layer_1_not_sigmoided = [round(sigmoided_der(i) * slope_layer_1_sigmoided[indx], 3) for indx, i in enumerate(layer_1)]
print("slope_layer_1_not_sigmoided = " + str(slope_layer_1_not_sigmoided))

#var input_list refers to: "processed data layer"
slope_wei_n_bias_1 = [[round(e * i, 4) for e in input_list] for i in slope_layer_1_not_sigmoided] 
print("slope_wei_n_bias_1 = " + str(slope_wei_n_bias_1))

learning_func = lambda layer_1, slope_layer_1, learn_rate: [[round(layer_1[indx_i][indx_e] - (e * learn_rate), 4) for indx_e, e in enumerate(i)] + [layer_1[indx_i][-1]] for indx_i, i in enumerate(slope_layer_1)]
learning_rate = -0.5
new_wei_n_bias_1 = learning_func(wei_n_bias_1, slope_wei_n_bias_1, learning_rate)
new_wei_n_bias_2 = learning_func(wei_n_bias_2, slope_wei_n_bias_2, learning_rate)  
new_wei_n_bias_answer = learning_func(wei_n_bias_answer, slope_wei_n_bias_answer, learning_rate) 

with open(layer_1_neuron, "w") as new_layer_1:
	new_layer_1.write(str(new_wei_n_bias_1))

with open(layer_2_neuron, "w") as new_layer_2:
	new_layer_2.write(str(new_wei_n_bias_2))

with open(layer_answer_neuron, "w") as new_layer_ans:
	new_layer_ans.write(str(new_wei_n_bias_answer))