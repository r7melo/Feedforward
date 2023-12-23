import json
import numpy as np
import pygame
from OpenGL.GL import *
from CG import App
from network_neural import NetworkNeural


class NetworkNeuralModel:
    def __init__(self, network_neural) -> None:
        self.data = [[0,0,0],[1,1,1],[-5,0,0]]
        self.network_neural:NetworkNeural = network_neural

    def update(self):

        glClearColor(0.2, 0.2, 0.2, 1.0)

        #region DATA
        for x,y,_y in self.data:
            if _y == 1: glColor3f(0,0,1)
            else: glColor3f(1,0,0)

            glPointSize(10)
            glBegin(GL_POINTS)
            glVertex2f(x,y)
            glEnd()
        #endregion

        proportion_screen = 500/30
        for x in range(30):
            for y in range(30):
                pos = {'x':x*proportion_screen, 'y':y*proportion_screen}

                input = np.array([1,1])
                _y = self.network_neural.feedforward(input)
                print(_y)
                if _y >= 0: glColor3f(.4,.4,1)
                else: glColor3f(1,.4,.4)
                glPointSize(10)
                glBegin(GL_POINTS)
                glVertex2f(pos['x'],pos['y'])
                glEnd()


class Program:
    def __init__(self):
        self.network_neural:NetworkNeural


    def mouse_button_up(self, event):
        if event.button == 1:
            print(f"Left: {event.pos}")
        elif event.button == 3:
            print(f"Right: {event.pos}")

    def save_perceptrons(self):
        with open('modelo.json', 'w') as arquivo:
            pJson = []
            json.dump(pJson, arquivo)
            print("salvo!")



if __name__=="__main__":
    
    app = App()
    app.screenSize = (500, 500)

    network_neural = NetworkNeural([2,2,1])
    
    program = Program()
    program.network_neural = network_neural

    network_neural_model = NetworkNeuralModel(network_neural)
    app.render.append(network_neural_model)

    app.event_actions[pygame.MOUSEBUTTONUP] = [program.mouse_button_up]
    app.start_thread(program.save_perceptrons, delay=10)

    app.run()