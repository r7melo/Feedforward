from random import random, randint
from scipy.special import expit

LEARNING_RATE = 0.3


class Perceptron:
    def __init__(self, bias=None, w:list=[]) -> None:
        self.score:int = 0
        self.bias:float = bias
        self.x:list = []
        self.w:list = w

        self.color3f = (random(), random(), random())

    def input(self, x:list) -> None:
        self.x = x
        
        if self.bias is None:
            self.bias = randint(-100,100)
            self.w = [randint(-100,100) for i in range(len(x))]

    def output(self) -> int:
        products = [ self.x[i]*self.w[i] for i in range(len(self.x)) ]
        S = sum(products+[self.bias])
        return 1 if S >= 0 else 0
        
    
    def correction(self, target:float, prediction:float) -> None:
        erro = target - prediction
        w = [(peso + LEARNING_RATE * erro * target) for peso in self.w]
        self.w = w

        bias = self.bias + LEARNING_RATE * erro * target
        self.bias

