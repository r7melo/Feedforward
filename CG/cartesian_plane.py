from OpenGL.GL import *

class CartesianPlane:
    def __init__(self):
        pass

    def show(self):
        glClearColor(0.2, 0.2, 0.2, 1.0)
        glBegin(GL_LINES)
        # # X
        # glColor3f(255,255,255)
        # glVertex2f(-6,0)
        # glVertex2f(6,0)
        # # Y
        # glColor3f(255,255,255)
        # glVertex2f(0,-6)
        # glVertex2f(0,6)

        # Left
        glColor3f(255,255,255)
        glVertex2f(-6,-6)
        glVertex2f(-6,6)
        # Right
        glColor3f(255,255,255)
        glVertex2f(6,-6)
        glVertex2f(6,6)
        # Top
        glColor3f(255,255,255)
        glVertex2f(-6,6)
        glVertex2f(6,6)
        # Botton
        glColor3f(255,255,255)
        glVertex2f(-6,-6)
        glVertex2f(6,-6)

        glEnd()

    def update(self):
        self.show()
        
