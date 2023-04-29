from Matrix import Matrix

class NeuralNetwork:

    def __init__(self, i_nodes, h_noudes, o_noudes):

        self.i_nodes = i_nodes
        self.h_nodes = h_noudes
        self.o_nodes = o_noudes

        self.bias_ih = Matrix((h_noudes, 1))
        self.bias_ih.randomize()
        self.bias_ho = Matrix((o_noudes, 1))
        self.bias_ho.randomize()

        self.weigths_ih = Matrix((h_noudes, i_nodes))
        self.weigths_ih.randomize()
        self.weigths_ho = Matrix((h_noudes, i_nodes))
        self.weigths_ho.randomize()

    def feedforeard(self, input):
        input = Matrix(input)
        hidden = self.weigths_ih * input
        print(hidden)
        