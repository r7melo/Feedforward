from random import randint

class T: pass

class Vector:

    def __init__(self, matrix):
        
        self.matrix = matrix

    def __mul__(self, other):

        matrix = Matrix((self.matrix.rows, self.matrix.cols))

        if self.matrix.rows != other.matrix.rows or self.matrix.cols != other.matrix.cols:
            raise ValueError("Matrix with unacceptable dimensions")

        for i in self.matrix.range_i:
            for j in self.matrix.range_j:
                matrix.data[i][j] = self.matrix.data[i][j] * other.matrix.data[i][j]

        return matrix

class Matrix:

    def __init__(self, data):

        self.rows = data[0] if type(data) is tuple else len(data) if type(data) is list else 0
        self.cols = data[1] if type(data) is tuple else len(data[0]) if type(data) is list else 0
        self.range_i = range(self.rows)
        self.range_j = range(self.cols)
        self.data = data if type(data) is list else [[0 for j in self.range_j] for i in self.range_i]

    def randomize(self):
        self.data = [[randint(-10000,10000) for j in self.range_j] for i in self.range_i]

    def map(self, other, func):

        if(self.rows != other.rows or self.cols != other.cols):
            raise ValueError("Matrix with different dimensions")

        matrix = Matrix((self.rows, self.cols))

        for i in self.range_i:
            for j in self.range_j:
                matrix.data[i][j] = func(self.data[i][j], other.data[i][j])

        return matrix

    def __str__(self):

        cols_widths = [max([len(str(self.data[i][j])) for i in self.range_i]) for j in self.range_j]
        return '\n'.join([(' '.join([str(self.data[i][j]).rjust(cols_widths[j]) for j in self.range_j])) for i in self.range_i])+'\n'
    
    def __add__(self, other):

        return self.map(other, lambda a, b: a + b)
    
    def __sub__(self, other):

        return self.map(other, lambda a, b: a - b)
    
    def __mul__(self, other):

        if type(other) is Matrix:
            if self.cols != other.rows:
                raise ValueError("Matrix with unacceptable dimensions")

            matrix = Matrix((self.rows, other.cols))

            for i in self.range_i:
                for j in other.range_j:
                    for k in self.range_j:
                        matrix.data[i][j] += self.data[i][k] * other.data[k][j]

            return matrix
        
        elif type(other) is int:

            matrix = Matrix((self.rows, self.cols))

            for i in self.range_i:
                for j in self.range_j:
                    matrix.data[i][j] = self.data[i][j] * other

            return matrix

        else:
            raise ValueError("Matrix not multipliable by this type of value")
        
    def __pow__(self, other):

        if other == T:
            
            matrix = Matrix((self.cols, self.rows))

            for i in self.range_i:
                for j in self.range_j:
                    matrix.data[j][i] = self.data[i][j]

            return matrix
        

