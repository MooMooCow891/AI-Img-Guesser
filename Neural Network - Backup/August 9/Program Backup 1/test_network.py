import numpy

input_layer = [3, 1]
layer_1 = [[6, -2], [-3, 5]]
layer_ans = [[1, 0.25], [-2, 2]]

euler = numpy.exp(1)
sigmoid = lambda x: round(1/(1 + euler**(-x)), 4)

def layer_process(lay_1, weights):
	layer_output = []
	for indx_wei, ele_wei in enumerate(weights):
		total = 0
		for indx_lay_1, ele_lay_1 in enumerate(lay_1):
			total += round(ele_lay_1 * ele_wei[indx_lay_1], 4)

		layer_output.append(round(sigmoid(total), 4))

	return layer_output

def der_wei(layer, der_not_sigmoided):
	return [[round(i * e, 4) for e in layer] for i in der_not_sigmoided]

def der_not_sigmoided(layer, der_sigmoided):
	return [round(i * (1 - i) * der_sigmoided[indx], 4) for indx, i in enumerate(layer)]

answer = 0
def der_cost_func(lis):
	return [2*(i - 1) if indx == answer else 2*(i - 0) for indx, i in enumerate(lis)]

def der_sigmoided(weights, der_not_sigmoided):
	return [round(sum([e * weights[indx_e][indx_i] for indx_e, e in enumerate(der_not_sigmoided)]), 4) for indx_i, i in enumerate(weights[0])]

output_layer_1 = layer_process(input_layer, layer_1)
output_layer_ans = layer_process(output_layer_1, layer_ans)

print(output_layer_1)
print(output_layer_ans)

der_sigmoided_ans = der_cost_func(output_layer_ans)
print(der_sigmoided_ans)

der_not_sigmoided_ans = der_not_sigmoided(output_layer_ans, der_sigmoided_ans)
print(der_not_sigmoided_ans)

der_wei_2 = der_wei(output_layer_1, der_not_sigmoided_ans)
print(der_wei_2)

der_layer_1_sigmoided = der_sigmoided(layer_ans, der_not_sigmoided_ans)
print(der_layer_1_sigmoided)

der_layer_1_not_sigmoided = der_not_sigmoided(output_layer_1, der_layer_1_sigmoided)
print(der_layer_1_not_sigmoided)

der_wei_1 = der_wei(input_layer, der_layer_1_not_sigmoided)
print(der_wei_1)