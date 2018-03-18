from matrix import Matrix

if __name__=="__main__":

	print("matrix1")
	matrix1 = Matrix(
			[1,2,3],
			[3,3,3], 
			[5,4,2]
			)
	print(matrix1)

	print("matrix1 + 1 = new_matrix1")
	new_matrix1 = matrix1 + 1
	print(new_matrix1)

	print("matrix2")
	matrix2 = Matrix(
			[6,7,8],
			[2,3,1], 
			[2,8,9]
			)
	print(matrix2)

	print("matrix1 + matrix2")
	new_matrix2 = matrix1 + matrix2
	print(new_matrix2)

	print("matrix1 * matrix2 = matrix3")
	matrix3 = matrix1*matrix2
	print(matrix3)


