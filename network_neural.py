import numpy as np

class NetworkNeural:
    def __init__(self, sizes) -> None:
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
    
    def sigmoid(self, z):
        return 1/(1+np.exp(-z))
    
    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = self.sigmoid((w @ input) + b)
        return a
