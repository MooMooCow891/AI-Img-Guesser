class EditFile: 
	def __init__(self, file_path: str, anew=False):
		self.file_path = file_path
		self.amend = False
		self.anew = anew
		self.clean = True

		if anew:
			with open(self.file_path, "w") as f:
				pass

	def __iter__(self):
		return iter([i for i in self.read().split("\n") if self.clean == False or self.clean == True and i != ""])

	def write_seg(self, string, new_line=True):
		with open(self.file_path, ("w", "a")[1 if self.amend else 0]) as f:
			f.write(f'{string}' + ("", "\n")[1 if new_line else 0])

		self.amend = True

	def clear(self):
		with open(self.file_path, "w") as f:
			self.amend = False

	def read(self, process=False):
		with open(self.file_path, "r") as f:
			return f.read()

	def set_iter_clean(self, inpt: bool):
		if isinstance(inpt, bool):
			self.clean = inpt
		else:
			raise ValueError("Input needs to be a boolean (True/False)")