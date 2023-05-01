from Matrix import Matrix


def dsigmoid (x):
    return x * (1-x)

class NeuralNetwork:

    def __init__(self, i_nodes, h_nodes, o_nodes):

        self.i_nodes = i_nodes
        self.h_nodes = h_nodes
        self.o_nodes = o_nodes

        self.bias_ih = Matrix((h_nodes, 1))
        self.bias_ih.randomize()
        self.bias_ho = Matrix((o_nodes, 1))
        self.bias_ho.randomize()

        self.weigths_ih = Matrix((h_nodes, i_nodes))
        self.weigths_ih.randomize()
        self.weigths_ho = Matrix((o_nodes, h_nodes))
        self.weigths_ho.randomize()

    def train(self, input, target):

        hidden = self.weigths_ih * Matrix(input)
        print(hidden)
        print(self.bias_ih)
        hidden = hidden + self.bias_ih
        print(hidden)
        hidden = [[dsigmoid(hidden[i][j]) for j in hidden.range_j] for i in hidden.range_i]
        print(hidden)



        


    
        