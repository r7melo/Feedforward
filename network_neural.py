import numpy as np

def print_array(array):
    def _(arr): return [_(i) if type(i) is np.ndarray else i for i in arr]
    print(_(array))
    

class NetworkNeural:
    def __init__(self, sizes) -> None:
        self.num_layers = len(sizes)
        self.sizes = sizes
        # self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        # self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
        self.biases = [np.random.randint(0,10, size=(y, 1)) for y in sizes[1:]]
        self.weights = [np.random.randint(0,10, size=(y, x)) for x, y in zip(sizes[:-1], sizes[1:])]
        
        
        self.learning_rate = 0.1
    
    def sigmoid(self, z):
        return 1/(1+np.exp(-z))
    
    def sigmoid_derivative(self, z):
        return self.sigmoid(z) * (1 - self.sigmoid(z))
    
    def feedforward(self, a): # a:input from layer
        for b, w in zip(self.biases, self.weights):
            a = self.sigmoid((w @ a) + b)
        return a

    def backpropagation(self, target, prediction):
        error = target - prediction

        for b, w in zip(self.biases, self.weights):
            derivative_output = self.sigmoid_derivative(prediction)
            delta_output = error * derivative_output
            print(delta_output)

    def training(self, targets_data, epochs):
        for epoch in range(1, epochs+1):
            for index, target in enumerate(targets_data, start=1):
                print(f"[epoch {epoch}] target {index}")


if __name__=="__main__":

    nn = NetworkNeural([2,2,1])
    input = np.array([1,1])
    output = nn.feedforward(input)
    nn.backpropagation(0, output)
