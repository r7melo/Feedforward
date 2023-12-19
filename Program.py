from OpenGL.GL import *
import pygame
from Perceptron import Perceptron
from CG import App, Mouse, Keyboard



class NetworkNeural:
    
    def __init__(self) -> None:
        self.data = [[0,0,0],[1,1,1],[-6,0,0]]
        self.perceptrons = [Perceptron() for i in range(10)]

    def training(self):
        for perceptron in self.perceptrons:
            #region PERCEPTRON LERANING
            for amostra in self.data:
                perceptron.input(amostra[:2])
                _y = perceptron.output()
                perceptron.correction(amostra[2], _y)
            #endregion

            for amostra in self.data:
                perceptron.input([amostra[0], amostra[1]])
                _y = perceptron.output()
                if amostra[2] == _y: perceptron.score+=1

    def update(self):
        glClearColor(0.2, 0.2, 0.2, 1.0)

        #region DATA
        for x,y,z in self.data:
            if z == 1: 
                glColor3f(0,0,1)
            else: glColor3f(1,0,0)

            glPointSize(10)
            glBegin(GL_POINTS)
            glVertex2f(x,y)
            glEnd()
        #endregion



class Program:
    def __init__(self):
        self.mouse:Mouse
        self.keyboard:Keyboard
        self.network_neural:NetworkNeural
            
    def start_mouse(self):
        while True:

            if self.mouse.left_button_release(): 
                x = (self.mouse.pos[0]-250)/35
                y = (self.mouse.pos[1]-250)/-35
                self.network_neural.data.append([x,y,1])
                    

            if self.mouse.right_button_release(): 
                x = (self.mouse.pos[0]-250)/35
                y = (self.mouse.pos[1]-250)/-35
                self.network_neural.data.append([x,y,0])  

            if len(self.network_neural.data) > 20:
                del(self.network_neural.data[0])


    def start_keyboard(self):
        while True:

            if self.keyboard.key_press and self.keyboard.key_press[pygame.K_ESCAPE]:
                print("ESCAPE")


if __name__=="__main__":
    
    app = App()
    app.screenSize = (500, 500)

    program = Program()
    program.mouse = Mouse()
    program.keyboard = Keyboard()
    program.network_neural = NetworkNeural()

    app.mouse = program.mouse
    app.keyboard = program.keyboard
    app.start_thread(program.start_mouse)
    app.start_thread(program.start_keyboard)

    app.render.append(program.network_neural)

    app.run()