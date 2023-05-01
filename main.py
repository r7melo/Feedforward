from Matrix import Matrix, Vector, T
from NeuralNetwork import NeuralNetwork


#nn = NeuralNetwork(1,6,1)

A = Matrix((1,3))
B = Matrix((1,3))
A.randomize()
B.randomize()
print(A)
print(B)
print(Vector(A)*Vector(B))
print(A**T)


input = [[1,2]]


#nn.feedforeard(input)



def GradientDescent(m, b):
    x = 0
    E = (m*x + b)**2

    m_ =0
    dm = E * x * m_
    db = E



"""
f = sigmoud

S1 = sum( f( Wo[1][n] * f( sum( W[i][j] * i[j] ) + b[i][n] ) ) ) + b[0][1]

"""