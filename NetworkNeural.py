from OpenGL.GL import *

from Perceptron import Perceptron



class NetworkNeuralGrafics:

    def __init__(self):
        self.data = [[1,1,1],[1,0,0],[0,1,0],[0,0,0]]
        self.perceptrons = [Perceptron() for i in range(10)]
        self.timeout = 0

    def show(self):

        #region DATA
        for x,y,z in self.data:
            if z == 1: glColor3f(0,0,255)
            else: glColor3f(255,0,0)

            glPointSize(10)
            glBegin(GL_POINTS)
            glVertex2f(x,y)
            glEnd()

        glBegin(GL_LINES)
        #endregion
        
        for perceptron in self.perceptrons:
            #region PERCEPTRON
            for amostra in self.data:
                data = [amostra[0], amostra[1]]
                perceptron.input(data)
                _y = perceptron.output()
                perceptron.correction(amostra[2], _y)

            for amostra in self.data:
                perceptron.input([amostra[0], amostra[1]])
                y = perceptron.output()
                if amostra[2] == y: perceptron.score+=1

            
        self.perceptrons.sort(key=lambda p: p.score)

        if self.timeout > 1000:
            for perceptron in self.perceptrons:
                perceptron.score = 0

            [self.perceptrons.pop() for i in range(5)]
            [self.perceptrons.append(Perceptron()) for i in range(5)]
        
        self.timeout += 1

        # functions perceptron
        glColor3f(0,255,0)
        for i in range(10):
            proportion = 6/10

            x1 = i*proportion
            x2 = i*proportion*2

            f = lambda x: sum([x * A for A in self.perceptrons[0].w] + [self.perceptrons[0].bias])

            glVertex2f(x1, f(x1))
            glVertex2f(x2, f(x2))
        #endregion

        glEnd()

    def update(self):
        self.show()
        

if __name__=="__main__":
    from CG import App, CartesianPlane 
    app = App()
    app.screenSize = (900, 900)
    app.render.append(CartesianPlane())
    app.render.append(NetworkNeuralGrafics())
    app.run()