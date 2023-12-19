import json
import threading
import time
from OpenGL.GL import *
import pygame

from Perceptron import Perceptron
from CG import App



class NetworkNeuralGrafics:

    def __init__(self, data):
        # blue:1 red:0
        self.data = data
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
            
            A = 1
            B = 1

            for i in self.data:
                if i[:-1] == 1: A+=1
                else: B+=1

            for amostra in self.data:
                perceptron.input([amostra[0], amostra[1]])
                _y = perceptron.output()
                if amostra[2] == _y and _y == 1: perceptron.score+= 100/A
                if amostra[2] == _y and _y == 0: perceptron.score+= 100/B


    def perceptron_classification(self):
        self.perceptrons.sort(key=lambda p: p.score)
        self.perceptrons.reverse()
        

        if self.timeout > 10:
            self.timeout = 0
            
            qtd_death = int(len(self.perceptrons)/2)
            better = self.perceptrons[0]
            self.perceptrons = self.perceptrons[:qtd_death] + [Perceptron(w=better.w) for i in range(qtd_death)]
            for p in self.perceptrons: p.score = 0

        self.timeout += 1

        for i in range(len(self.perceptrons)):
            if i == 0:
                self.perceptrons[i].color3f = (1,0,0)
            else:
                opc = 1-(1/i)
                self.perceptrons[i].color3f = (opc,opc,opc)

    def show(self):

        
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

        
        perceptron = self.perceptrons.copy()[0]
        proportion = 6/20
        for i in range(-19, 20):
            for j in range(-19, 20):


                x = i*proportion
                y = j*proportion

                perceptron.input([x,y])
                _y = perceptron.output()

                if _y == 1: glColor3f(0.41,0.41,.99)
                else: glColor3f(0.99, 0.41, 0.41)

                glPointSize(10.5)
                glBegin(GL_POINTS)
                glVertex2f(x,y)
                glEnd()
                    




    def save_perceptrons(self):
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
        
        threading.Timer(10, self.save_perceptrons).start()

    def traing(self):
        while True:
            time.sleep(.1)
            self.perceptron_classification()
            self.perceptron_training_epoch()
            

    def update(self):
        self.show()
        







data = [
     [-1.5, 2.5, 0],
    [1.0, -3.0, 1]
]


def append_data():
    try:
        mouse = {
            "pos":pygame.mouse.get_pos(),
            "left_button":pygame.mouse.get_pressed()[0],
            "right_button":pygame.mouse.get_pressed()[2]
        }

        if mouse["left_button"]:
            pos = mouse["pos"]
            x = ((pos[0]-40)/420*12)-6
            y = (((pos[1]-40)/420*12)-6)*-1
            if -6 < x < 6 and -6 < y < 6: data.append([x,y,1])

        if mouse["right_button"]:
            pos = mouse["pos"]
            x = ((pos[0]-40)/420*12)-6
            y = (((pos[1]-40)/420*12)-6)*-1
            if -6 < x < 6 and -6 < y < 6: data.append([x,y,0])

    except:pass

    threading.Timer(0.2, append_data).start()





if __name__=="__main__":
    nng = NetworkNeuralGrafics(data)
    thread = threading.Thread(target=nng.traing)
    thread.daemon = True
    thread.start()

    save = threading.Thread(target=nng.save_perceptrons)
    save.daemon = True
    save.start()
     
    app = App()
    app.screenSize = (500, 500)
    app.render.append(nng)

    mouse = threading.Thread(target=append_data)
    mouse.daemon = True
    mouse.start()


    app.run()