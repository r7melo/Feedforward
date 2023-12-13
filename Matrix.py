class Matrix:

    """
    Recebe uma lista unidimensional ou multimedição
    Ex.: matrix pode ser [0], [0,1], [[0,9],[1,2],[2,1]]

    - Propriedades:
        > Todas as sub-listas obrigatoriamente terão a mesma quantidade de colunas/linhas.

    """
    def __init__(self, matrix:list):

        self.rows:int = 0
        self.cols:int = 0
        self.range_i:range = None
        self.range_j:range = None
        self.data:list = []

        if matrix is list:
            if matrix fo
        else:
            raise ValueError("Object is not an array")

    def map(self, other, func):

        if other is not None and (self.rows != other.rows or self.cols != other.cols):
            raise ValueError("Matrix with different dimensions")

        matrix = Matrix((self.rows, self.cols))

        for i in self.range_i:
            for j in self.range_j:
                if other == None:
                    matrix.data[i][j] = func(matrix.data[i][j])
                else:
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
        


