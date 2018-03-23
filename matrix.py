class Matrix:

	def __init__(self,*rows):
		for row in rows:
			if not isinstance(row, list):
				raise TypeError("It is not a row for matrix")
			if len(row) != len(rows[0]):
				raise TypeError("Size of columns is not the same")
			for element in row:
				if not isinstance(element, (int, float)):
					raise TypeError("Element '"+str(element)+"' is not a number")
		
		self.matrix = [] 
		for row in rows:
			self.matrix.append(row) 
		self.rows = len(self.matrix)
		self.columns = len(self.matrix[0])
		

	def myGenerator(self):
		for row in self.matrix:
			yield row
	
	
		
	def __str__(self):
		result = "Matrix:" + str(self.rows) + "x" + str(self.columns) + "\n"
		for row in self.myGenerator():
			result += str(row) + "\n"
		return result


	def plus(self,matrix2):
		if self.rows == matrix2.rows and self.columns == matrix2.columns:
			print("add matrix2")
			new_matrix = []
			for row in range(0,self.rows):
				new_matrix.append([])
				for column in range(0,self.columns):
					new_matrix[row].append(self.matrix[row][column] + matrix2.matrix[row][column])	
			return Matrix(*new_matrix)
		else:
			raise TypeError("Sizes of matrixs are not the same")

	def sub(self,matrix2):
		if self.rows == matrix2.rows and self.columns == matrix2.columns:
			print("add matrix2")
			new_matrix = []
			for row in range(0,self.rows):
				new_matrix.append([])
				for column in range(0,self.columns):
					new_matrix[row].append(self.matrix[row][column] - matrix2.matrix[row][column])	
			return Matrix(*new_matrix)
		else:
			raise TypeError("Sizes of matrixs are not the same")


	def __add__(self, rightObject):
		if  isinstance(rightObject, (int,float)):
			new_matrix = []
			for row in range(0,self.rows):
				new_matrix.append([])
				for column in range(0,self.columns):
					new_matrix[row].append(self.matrix[row][column] + rightObject)
			return Matrix(*new_matrix)
		elif isinstance(rightObject,Matrix): 
			return self.plus(rightObject)
		else:
			raise TypeError("Element '" + str(rightObject) + "' is not a number")

	def __radd__(self, leftObject):
		if  isinstance(leftObject, (int,float)):
			new_matrix = []
			for row in range(0,self.rows):
				new_matrix.append([])
				for column in range(0,self.columns):
					new_matrix[row].append(self.matrix[row][column] + leftObject)
			return Matrix(*new_matrix)
		elif isinstance(leftObject,Matrix): 
			return self.plus(leftObject)
		else:
			raise TypeError("Element '" + str(leftObject) + "' is not a number")

	def __sub__(self, rightObject):
		if  isinstance(rightObject, (int,float)):
			new_matrix = []
			for row in range(0,self.rows):
				new_matrix.append([])
				for column in range(0,self.columns):
					new_matrix[row].append(self.matrix[row][column] - rightObject)
			return Matrix(*new_matrix)
		elif isinstance(rightObject,Matrix): 
			return self.sub(rightObject)
		else:
			raise TypeError("Element '" + str(rightObject) + "' is not a number")

	def __rsub__(self, leftObject):
		if  isinstance(leftObject, (int,float)):
			new_matrix = []
			for row in range(0,self.rows):
				new_matrix.append([])
				for column in range(0,self.columns):
					new_matrix[row].append(self.matrix[row][column] - leftObject)
			return Matrix(*new_matrix)
		elif isinstance(leftObject,Matrix): 
			return self.sub(leftObject)
		else:
			raise TypeError("Element '" + str(leftObject) + "' is not a number")



	def mul(self,matrix2):
		new_matrix = []
		for i in range(0,self.rows):
			new_matrix.append([])
			for j in range(0,matrix2.columns):
				new_element = [self.matrix[i][k] * matrix2.matrix[k][j] for k in range(0,self.columns)]				
				new_matrix[i].append(sum(new_element))
				
		return Matrix(*new_matrix)		


	def __mul__(self,rightObject):

		if  isinstance(rightObject, (int,float)):
			new_matrix = []
			for row in range(0,self.rows):
				new_matrix.append([])
				for column in range(0,self.columns):
					new_matrix[row].append(self.matrix[row][column] * rightObject)
			return Matrix(*new_matrix)
		elif isinstance(rightObject,Matrix): 
			if self.columns == rightObject.rows:
				return self.mul(rightObject)
			else:
				raise TypeError("Number of columns of left matrix equal to the number of rows of right matrix ")
		else:
			raise TypeError("Element '" + str(rightObject) + "' is not a number")

	def __rmul__(self,leftObject):

		if  isinstance(leftObject, (int,float)):
			new_matrix = []
			for row in range(0,self.rows):
				new_matrix.append([])
				for column in range(0,self.columns):
					new_matrix[row].append(self.matrix[row][column] * leftObject)
			return Matrix(*new_matrix)
		elif isinstance(leftObject,Matrix): 
			if self.columns == leftObject.rows:
				return self.mul(leftObject)
			else:
				raise TypeError("Number of columns of left matrix equal to the number of rows of right matrix ")
		else:
			raise TypeError("Element '" + str(leftObject) + "' is not a number")
				
			
			
def function():
	print("__name__=='__main__'. This should not be printed")

if __name__ == '__main__':
	function()			

	
		
		
