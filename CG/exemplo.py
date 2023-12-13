from math import *
from OpenGL.GL import *



class Circle:

    # FUNÇÃO QUALQUER PARA SER REPRESENTADA
    def f(self, x):
        a = abs(x) - 1
        b = 1 - pow(a, 2)
        if b < 0:
            return 0
        else:
            return sqrt(b)

    def h(self, x):
        a = abs(x)/2
        b = 1-sqrt(a)
        if b < 0:
            b = 0
        return -2.5*sqrt(b)

    def g(self, x,y, angle):
        return ( (y * cos((angle/180)*pi)) - (x * sin((angle/180)*pi)), (y * sin((angle/180)*pi)) + (x * cos((angle/180)*pi)))


    def coracao(self):
        dx = 0.1
        glBegin(GL_POLYGON)
        glColor3f(1,0,0)

        x = -2
        while -2 <= x <0:
            glVertex3f(x, self.f(x), 0)
            glVertex3f(x+dx, self.f(x+dx), 0)
            x += dx
        glEnd()

        glBegin(GL_POLYGON)
        x = 0
        while 0 <= x <= 2:
            glVertex3f(x, self.f(x), 0)
            glVertex3f(x+dx, self.f(x+dx), 0)
            x += dx
        glEnd()

        glBegin(GL_POLYGON)

        x = -2
        while -2 <= x < 2:
            glVertex3f(x, self.h(x), 0)
            glVertex3f(x+dx, self.h(x+dx), 0)
            x += dx
        glEnd()

        

    def circle(self, angle_z=0):
        angle = 0
        dz = 10
        rain = 3

        glBegin(GL_LINES)
        glColor3f(0,1,0.7)

        
        while 0 <= angle < 360:

            glVertex3f(self.g(0,rain,angle)[0], self.g(0,rain,angle)[1], angle_z)
            glVertex3f(self.g(0,rain,angle+dz)[0], self.g(0,rain,angle+dz)[1], angle_z)

            angle += dz
            
        glEnd()

    def esfera(self):
        angle = 0
        dy = 10

        while 0 <= angle < 360:
            self.circle(self.g(0,5,angle)[1])
            angle += dy
        

        

    def update(self):
        
        self.circle()
        self.coracao()



if __name__=="__main__":
        from app import App
        from cartesian_plane import CartesianPlane
        app = App()
        app.screenSize = (900, 900)
        app.render.append(CartesianPlane())
        app.render.append(Circle())
        app.run()