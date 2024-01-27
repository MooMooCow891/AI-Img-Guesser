from avg_ele_list import list_get_avg

check = lambda x: int(x) if x % 1 == 0 else x

def matrix_get_avg(*inputs: list | tuple):
	error_list = [False for i in inputs 
			   	  if isinstance(i, list) == False and isinstance(i, tuple) == False]

	s_plural = ["", "s"][0 if len(inputs) > 1 else 1]
	false_inpt =  [f'Input {indx + 1}' for indx, i in enumerate(error_list) if i == False]
	type_false_inpt =  set([f'{type(i)}' for i in inputs if isinstance(i, list) == False])

	if all(error_list) == False:
		raise ValueError(f'Invalid input{", ".join(s_plural)}: {", ".join(false_inpt)}. Please use lists or tuples or sets instead of {", ".join(type_false_inpt)}')

	


	# len_check_list = len(set([len(i) for i in inputs]))
	# if len_check_list == 0:
	# 	return []
	# elif len_check_list > 1:
	# 	raise ValueError("Inputs must have the same amount of element")

	#return [check(sum([e[indx_i] for e in inputs])/len(inputs)) for indx_i, i in enumerate(inputs[0])]

	# for indx_i, i in enumerate(inputs[0]):
	# 	assert isinstance(inputs[0], list)

	# 	for e in inputs:
	# 		assert isinstance(e, list)

	# 		print(e[indx_i])

tensor_3d = [[[1, 2, 3], [4, 5, 6]], 
			 [[7, 8, 9], [10, 11, 12]], 
			 [[13, 14, 15], [16, 17, 18]]]

test = (1, 2, 3)

print(matrix_get_avg(tensor_3d))