import json
import threading
import time
from OpenGL.GL import *
from Perceptron import Perceptron
from CG import App, Mouse
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




class Program:
    def __init__(self):
        self.mouse:Mouse
        self.network_neural:NetworkNeural
            
    def init_mouse(self):

        def left_button_activate(pos):
            x = (pos[0]-250)/35
            y = (pos[1]-250)/-35
            self.network_neural.data.append([x,y,1])

        def right_button_activate(pos):
            x = (pos[0]-250)/35
            y = (pos[1]-250)/-35
            self.network_neural.data.append([x,y,0])
                
        self.mouse.left_button_activate = left_button_activate
        self.mouse.right_button_activate = right_button_activate

    def save_perceptrons(self):
        with open('modelo.json', 'w') as arquivo:
            pJson = []
            json.dump(pJson, arquivo)
        
        threading.Timer(10, self.save_perceptrons).start()


if __name__=="__main__":
    
    app = App()
    app.screenSize = (500, 500)

    program = Program()
    program.mouse = Mouse()
    program.network_neural = NetworkNeural()

    app.mouse = program.mouse
    program.init_mouse()

    app.render.append(program.network_neural)

    app.start_thread(program.network_neural.training)
    app.start_thread(program.network_neural.update_grid)
    app.start_thread(program.save_perceptrons)

    app.run()