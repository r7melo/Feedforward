import json
import threading
import time
from OpenGL.GL import *
from Perceptron import Perceptron
from CG import App, Mouse



class NetworkNeural:
    
    def __init__(self) -> None:
        self.data = [[0,0,0],[1,1,1]]
        self.perceptron = Perceptron()
        self.grid = []
        self.epoch = 0

    def training(self):
        while True:

            #region PERCEPTRON LERANING
            for amostra in self.data:
                self.perceptron.input(amostra[:2])
                _y = self.perceptron.output()
                self.perceptron.correction(amostra[2], _y)
            #endregion        

            time.sleep(0.1)


    def update_grid(self):
        while True:
            grid = []
            proportion = 6/20
            for i in range(-19, 20):
                for j in range(-19, 20):


                    x = i*proportion
                    y = j*proportion

                    self.perceptron.input([x,y])
                    _y = self.perceptron.output()
                    grid.append([x,y,_y])

            self.grid = grid

            time.sleep(1)

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
        
        for x,y,_y in self.grid:
            if _y == 1: glColor3f(0.41,0.41,.99)
            else: glColor3f(0.99, 0.41, 0.41)

            glPointSize(10.5)
            glBegin(GL_POINTS)
            glVertex2f(x,y)
            glEnd()



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

    app.run()