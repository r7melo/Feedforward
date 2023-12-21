import random
import numpy as np

def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    return sigmoid(z) * (1 - sigmoid(z))

class NetworkNeural:
    def __init__(self, sizes) -> None:
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid((w @ a) + b)
        return a
    
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        training_data = list(training_data)
        n = len(training_data)

        if test_data:
            test_data = list(test_data)
            n_test = len(test_data)

        for j in range(epochs):
            random.shuffle(training_data)
            mini_batchs = [training_data[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)]

            for mini_batch in mini_batchs:
                self.update_mini_batch(mini_batch, eta)

            if test_data:
                print(f"Epoch {j} : {self.evaluate(test_data)} / {n_test}")
            else:
                print(f"Epoch {j} finalizada")

    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]

        
        self.weights = [w - (eta/len(mini_batch)) * nw for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b - (eta/len(mini_batch)) * nb for b, nb in zip(self.biases, nabla_b)]


    def backprop(self, x, y):

        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        # FeedForward
        activation = x

        # Lista para armazenar todas as ativaçãoes, camada por camada
        activations:list[np.array] = [x]

        # Lista para armazenar todos os vetores z, camada por camada
        zs = []

        for b, w in zip(self.biases, self.weights):
            z = (w @ activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        # Backward pass
        delta = self.cost_derivative(activation[-1], y) * sigmoid(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = delta @ activations[-1].transpose()

        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = (self.weights[-l+1].transpose() @ delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = delta.reshape((-1, 1)) @ activations[-l-1].reshape((1, -1))



        return (nabla_b, nabla_w)
    
    def cost_derivative(self, output_activations, y):
        return output_activations - y
    
    @staticmethod
    def generate_data(num_samples):
        inputs = np.random.rand(num_samples, 2) 
        labels = (inputs[:, 0] + inputs[:, 1]).reshape((num_samples, 1)) 
        return list(zip(inputs, labels))

if __name__=="__main__":

    nn = NetworkNeural([2, 3, 1])
    training_data = NetworkNeural.generate_data(1000)
    nn.SGD(training_data, epochs=10, mini_batch_size=10, eta=0.1)

    # Agora a rede neural está treinada. Você pode fazer previsões para novos dados.
    input_example = np.array([0.2, 0.4])
    output_prediction = nn.feedforward(input_example)
    print("Entrada:", input_example)
    print("Saída Prevista:", output_prediction)