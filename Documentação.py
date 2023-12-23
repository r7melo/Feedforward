import random
import numpy as np

# sigmoid: funão de ativação usada no nosso exemplo
def sigmoid(z):
    return 1/(1+np.exp(-z))


"""
Para uma rede neural com duas entradas, duas camadas ocultas e 
uma saída, podemos representar essa rede, precisaremos montar seus pesos e biases.

Biases -> (
    [
        b1,
        b2
    ],
    [
        b3
    ]
)

Pesos -> (
    [
        [w1, w2],
        [w3, w4]
    ],
    [
        w5,
        w6
    ]
)

Exemplo: para rede neural de tamanho [2,2,1], obtemos a primeira camada,

Exemplo de input -> (
    [
        x1,
        x2
    ]
)

Produto escalar da camada 1:
    PE1 = [
        w1*x1 + w2*x2
        w3*x1 + w4*x2
    ]

Função de ativação dos valores da camada 1:
    output1 = [
        sigmoid( PE1[0] + b1),
        sigmoid( PE1[1] + b2)
    ]

    ou 

    output1 = [
        sigmoid( (w1*x1 + w2*x2) + b1),
        sigmoid( (w3*x1 + w4*x2) + b2)
    ]

Finalizando o ciclo da rede.
Produto escalar da camada final:
    PE2 = [
        (output1[0] * w5) + output1[1] * w6)
    ] 

    ou 

    PE2 = [
        (sigmoid( (w1*x1 + w2*x2) + b1) * w5) + (sigmoid( (w3*x1 + w4*x2) + b2) * w6)
    ] 

Função de ativação dos valores da camada 1:
    output2 = [
        sigmoid( PE2[0] + b3)
    ] 

    ou

    output2 = [
        sigmoid( (sigmoid( (w1*x1 + w2*x2) + b1) * w5) + (sigmoid( (w3*x1 + w4*x2) + b2) * w6) + b3)
    ]   


Concluindo, para uma rede neural [2,2,1] obtemos:
    output = sigmoid( (sigmoid( (w1*x1 + w2*x2) + b1) * w5) + (sigmoid( (w3*x1 + w4*x2) + b2) * w6) + b3)

"""
class NetworkNeural:
    def __init__(self, sizes) -> None:
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid((w @ input) + b) # Numpy consegue usar a função sigmoid uma vez, mas retornado o array processado
        return a



nn = NetworkNeural([2,2,1])

input = np.array([1,1])
output = nn.feedforward(input)
print(output)


