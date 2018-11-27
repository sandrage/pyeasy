
def identity(size):
    return [[(i==j and 1) or 0 for i in range(0,size)] for j in range(0,size)]
def square(size):
    return [[(i*size)+j for j in range(0,size)] for i in range(0,size)]

def transpose(matrix):
    return [[matrix[j][i] for j in range(0,len(matrix))] for i in range(0,len(matrix[0]))]

def sum_product(row,column):
    return sum([i[0] * i[1] for i in zip(row,column)])
def get_column(matrix, column_number):
    return [matrix[i][column_number] for i in range(0,len(matrix))]

def multiply(matrix_one, matrix_two):
    if len(matrix_one[0]) != len(matrix_two):
        raise ArgumentException
    return [[sum_product(matrix_one[i], get_column(matrix_two,j)) for j in range(0,len(matrix_two[i]))] for i in range(0,len(matrix_one))]

if __name__=='__main__':
    print(identity(5))
    print(square(5))
    print(transpose(square(5)))
    print(transpose([[1,2],[3,4],[5,6]]))
    print(sum_product([1,2,3],[1,2,3]))
    print(multiply([[1,2,3]],[[1],[2],[3]]))
