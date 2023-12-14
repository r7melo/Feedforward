import json
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
                S = perceptron.output()
                _y = perceptron.activate(S)
                perceptron.correction(amostra[2], _y)
            #endregion

            for amostra in self.data:
                perceptron.input([amostra[0], amostra[1]])
                S = perceptron.output()
                _y = perceptron.activate(S)
                if amostra[2] == _y: perceptron.score+=1

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

        perceptrons:list[Perceptron] = self.perceptrons.copy()
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
                
                perceptron.input([x1,0])
                y1 = perceptron.output()

                perceptron.input([x2,0])
                y2 = perceptron.output()

                glVertex2f(x1, y1)
                glVertex2f(x2, y2)


            glEnd()

    def save_perceptrons(self):
        while True:
            with open('perceptrons.json', 'w') as arquivo:
                pJson = [
                    {
                        "bias": p.bias,
                        "w": [
                            w for w in p.w    
                        ],
                    }
                    for p in self.perceptrons
                ]
                json.dump(pJson, arquivo)
            time.sleep(10)

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

    save = threading.Thread(target=nng.save_perceptrons)
    save.daemon = True
    save.start()
     
    app = App()
    app.screenSize = (900, 900)
    app.render.append(CartesianPlane())
    app.render.append(nng)
    app.run()