from Matrix import Matrix, Vector, T
from NeuralNetwork import NeuralNetwork


nn = NeuralNetwork(1,3,2)
input = [[1,2]]
nn.train(input, [0,1])