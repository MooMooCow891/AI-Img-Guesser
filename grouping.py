def group(inpt: list | tuple, *names: str | int) -> dict:
	for name in names:
		return {f'{name}_{indx + 1}': i for indx, i in enumerate(inpt)}


# lis = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
# print(group(lis, "Yes", "No"))

def layer_test(nested_lis): # Credit: Bing Chat for optimizing the original function
    if isinstance(nested_lis, list):
        return 1 + layer_test(nested_lis[0])
    else:
        return 0


print(layer_test([[[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]], [[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]]]))