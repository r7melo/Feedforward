import threading
import time
from OpenGL.GL import *

from Perceptron import Perceptron
from CG import App, CartesianPlane



class NetworkNeuralGrafics:

    def __init__(self):
        self.data = [[1,1,1],[1,0,0],[0,1,0],[0,0,0],[0,2,1]]
        self.perceptrons = [Perceptron() for i in range(10)]
        self.timeout = 0
        
    def perceptron_training_epoch(self):
        for perceptron in self.perceptrons:
            #region PERCEPTRON LERANING
            for amostra in self.data:
                data = [amostra[0], amostra[1]]
                perceptron.input(data)
                _y = perceptron.output()
                perceptron.correction(amostra[2], _y)
            #endregion

            for amostra in self.data:
                perceptron.input([amostra[0], amostra[1]])
                y = perceptron.output()
                if amostra[2] == y: perceptron.score+=1

    def perceptron_classification(self):
        self.perceptrons.sort(key=lambda p: p.score)
        self.perceptrons.reverse()
        

        if self.timeout > 10:
            self.timeout = 0
            
            qtd_death = int(len(self.perceptrons)/2)
            self.perceptrons = self.perceptrons[:qtd_death] + [Perceptron() for i in range(qtd_death)]
            for p in self.perceptrons: p.score = 0

        self.timeout += 1

        for i in range(len(self.perceptrons)):
            if i == 0:
                self.perceptrons[i].color3f = (1,0,0)
            else:
                opc = 1-(1/i)
                self.perceptrons[i].color3f = (opc,opc,opc)

    def show(self):

        perceptrons = self.perceptrons.copy()
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

        
        for perceptron in perceptrons[:5]:

            glColor3f(perceptron.color3f[0], perceptron.color3f[1], perceptron.color3f[2])
            glBegin(GL_LINES)

            # functions perceptron
            for i in range(-1000,1000):
                proportion = 6/1000

                x1 = i*proportion
                x2 = i*proportion*2

                f = lambda x: sum([x * A for A in perceptron.w] + [perceptron.bias])

                y1 = f(x1)
                y2 = f(x2)

                glVertex2f(x1, y1)
                glVertex2f(x2, y2)


            glEnd()

        print([p.score for p in perceptrons[:5]])


    def traing(self):
        while True:
            self.perceptron_classification()
            self.perceptron_training_epoch()
            time.sleep(.1)

    def update(self):
        self.show()
        

if __name__=="__main__":
    nng = NetworkNeuralGrafics()
    thread = threading.Thread(target=nng.traing)
    thread.daemon = True
    thread.start()
     
    app = App()
    app.screenSize = (900, 900)
    app.render.append(CartesianPlane())
    app.render.append(nng)
    app.run()