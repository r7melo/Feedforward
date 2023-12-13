from scipy.special import expit
from random import randint

LEARNING_RATE = 0.5


class Perceptron:
    def __init__(self) -> None:
        self.score:int = 0
        self.bias:float = None
        self.x:list = []
        self.y:list = []

    def input(self, x:list) -> None:
        self.x = x
        
        if self.bias is None:
            self.bias = randint(-100,100)
            self.w = [randint(-100,100) for i in range(len(x))]

    def output(self) -> int:
        products = [ self.x[i]*self.w[i] for i in range(len(self.x)) ]
        S = sum(products+[self.bias])
        return 1 if expit(S) >= 0.5 else 0
    
    def correction(self, target:float, prediction:float) -> None:
        erro = target - prediction
        w = [(peso + LEARNING_RATE * erro * target) for peso in self.w]
        self.w = w

        bias = self.bias + LEARNING_RATE * erro * target
        self.bias


if __name__=="__main__":

    dataEND = [
        [1,1,1],
        [1,0,0],
        [0,1,0],
        [0,0,0]
    ]

    dataOR = [
        [1,1,1],
        [1,0,1],
        [0,1,1],
        [0,0,0]
    ]

    score = 0
    while score < 4:
        score = 0

        perceptron = Perceptron()

        for epoca in range(100000):
            for amostra in dataEND:
                data = [amostra[0], amostra[1]]
                perceptron.input(data)
                y = perceptron.output()
                perceptron.correction(amostra[2], y)

        
        for data in dataEND:
            perceptron.input([data[0], data[1]])
            y = perceptron.output()
            print(f"data={data} y={y}")

            if data[2] == y: score+=1
        
        print("")

   