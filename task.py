
class Matrix22:
    
    matrix = [0,0,0,0]
    
    def __init__(self,m1,m2,m3,m4):
            self.matrix = [m1,m2,m3,m4]
    
    def sum(self):
        suma = 0
        for m in self.matrix:
            suma = suma + m
        return suma
    
    
    def prod(self, mat2):
        #print(str(self.matrix[0]))
        m1 = (self.matrix[0]*mat2.matrix[0]) + (self.matrix[1]*mat2.matrix[2])
        m3 = (self.matrix[2]*mat2.matrix[0]) + (self.matrix[3]*mat2.matrix[2])
        m2 = (self.matrix[0]*mat2.matrix[1]) + (self.matrix[1]*mat2.matrix[3])
        m4 = (self.matrix[2]*mat2.matrix[1]) + (self.matrix[3]*mat2.matrix[3])
        mat12 = Matrix22(m1,m2,m3,m4)
        return mat12
    def show(self):
        print("["+str(self.matrix[0]) + " " + str(self.matrix[1])+"]")
        print("["+str(self.matrix[2]) + " " + str(self.matrix[3])+"]")
        pass
        
   


matrix_1  = Matrix22(1,2,3,4)    
matrix_2 = Matrix22(2,2,2,1)

matrix_3 = matrix_1.prod(matrix_2)
mat1_sum = matrix_3.sum()
print ("matrix_3: sum = " + str(mat1_sum))

print ("Matrix3:")
matrix_3.show()
