from Main_AI_Part import layer_1, layer_2, layer_ans, wei_n_bias_1, wei_n_bias_2, wei_n_bias_answer
import numpy

euler = numpy.exp(1)
error_slope = lambda dic: [2*(value - 1) if key == "3" else 2*(value - 0) for key, value in dic.items()]
sigmoided_der = lambda sigmoided_func: round(sigmoided_func * (1 - sigmoided_func), 2)
print(layer_ans)

slope_of_error = dict(zip(["3", "bee"], error_slope(layer_ans)))
print("Error Cost slope = " + str(slope_of_error))

slope_layer_ans = dict(zip(["3", "bee"], [sigmoided_der(value)*slope_of_error[key] for key, value in layer_ans.items()]))
print("slope layer ans = " + str(slope_layer_ans))

slope_wei_n_bias_answer = [[round(e * slope_layer_ans["3"], 3) if indx == 0 else round(e * slope_layer_ans["bee"], 3) for e in i[:-1]] for indx, i in enumerate(wei_n_bias_answer)]
"""
for indx, i in enumerate(wei_n_bias_answer):
	for e in i:
		if indx == 0:
			round(e * slope_layer_ans["3"], 3) #round to the thousandth
		else:
			round(e * slope_layer_ans["bee"], 3) #round to the thousandth
"""
print("slope_wei_n_bias_answer = " + str(slope_wei_n_bias_answer))

weights_for_3 = wei_n_bias_answer[0][:-1]
slope_layer_2_sigmoided = [round(sum([item * i if key == "3" else item * wei_n_bias_answer[1][indx] for key, item in slope_layer_ans.items()]), 3) for indx, i in enumerate(weights_for_3)]
print("slope_layer_2_sigmoided = " + str(slope_layer_2_sigmoided))

slope_layer_2_not_sigmoided = [round(sigmoided_der(i) * slope_layer_2_sigmoided[indx], 3) for indx, i in enumerate(layer_2)]
print("slope layer 2 not sigmoided = " + str(slope_layer_2_not_sigmoided))

slope_wei_n_bias_2 = [[round(e * slope_layer_2_not_sigmoided[indx], 3)  for e in i[:-1]] for indx, i in enumerate(wei_n_bias_2)]
print("slope_wei_n_bias_2 = " + str(slope_wei_n_bias_2))

slope_layer_1_sigmoided = [round(sum([e * wei_n_bias_2[indx_2][indx_1] for indx_2, e in enumerate(slope_layer_2_not_sigmoided)]), 3) for indx_1, i in enumerate(wei_n_bias_2[0][:-1])]
print("slope_layer_1_sigmoided = " + str(slope_layer_1_sigmoided))

slope_layer_1_not_sigmoided = [round(sigmoided_der(i) * slope_layer_1_sigmoided[indx], 3) for indx, i in enumerate(layer_1)]
print("slope_layer_1_not_sigmoided = " + str(slope_layer_1_not_sigmoided))

slope_wei_n_bias_1 = [[round(e * slope_layer_1_not_sigmoided[indx], 3) for e in i[:-1]] for indx, i in enumerate(wei_n_bias_1)]
print("slope_wei_n_bias_1 = " + str(slope_wei_n_bias_1))