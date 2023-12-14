from OpenGL.GL import *

from Perceptron import Perceptron



class NetworkNeuralGrafics:

    def __init__(self):
        self.data = [[1,1,1],[1,0,0],[0,1,0],[0,0,0]]
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

            perceptron.score = 0
            for amostra in self.data:
                perceptron.input([amostra[0], amostra[1]])
                y = perceptron.output()
                if amostra[2] == y: perceptron.score+=1

            
        self.perceptrons.sort(key=lambda p: p.score)


    def show(self):
        glClearColor(0.2, 0.2, 0.2, 1.0)
        #region DATA
        for x,y,z in self.data:
            if z == 1: 
                glColor3f(0,0,255)
            else: glColor3f(255,0,0)

            glPointSize(10)
            glBegin(GL_POINTS)
            glVertex2f(x,y)
            glEnd()
        #endregion

        
        for perceptron in self.perceptrons:

            glColor3f(perceptron.color3f[0], perceptron.color3f[1], perceptron.color3f[2])
            glBegin(GL_LINES)

            # functions perceptron
            for i in range(5):
                proportion = 6/10

                x1 = i*proportion
                x2 = i*proportion*2

                f = lambda x: sum([x * A for A in perceptron.w] + [perceptron.bias])

                glVertex2f(x1, f(x1))
                glVertex2f(x2, f(x2))

            glEnd()

    def update(self):
        self.perceptron_training_epoch()
        self.show()
        

if __name__=="__main__":
    from CG import App, CartesianPlane 
    app = App()
    app.screenSize = (900, 900)
    app.render.append(CartesianPlane())
    app.render.append(NetworkNeuralGrafics())
    app.run()