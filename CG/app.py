import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class App:
    def __init__(self):
        self.rot = 0
        self.render = []
        self.speed = 3
        self.sum_rot_updown = 0
        self.current_mv_mat = (GLfloat * 16)()
        self.screenSize = (500, 500)

    def run(self):
        pygame.init()

        
        pygame.display.set_mode(self.screenSize, DOUBLEBUF | OPENGL)


        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (self.screenSize[0] / self.screenSize[1]), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)   
        glEnable(GL_DEPTH_TEST)
        glTranslate(0, 0, -50 / self.speed)


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_ESCAPE]:
                pygame.quit()
                quit()

            glGetFloatv(GL_MODELVIEW_MATRIX, self.current_mv_mat)
            glLoadIdentity()
            glMultMatrixf(self.current_mv_mat)
            glPushMatrix()

            glGetFloatv(GL_MODELVIEW_MATRIX, self.current_mv_mat)
            glLoadIdentity()
            glRotatef(self.sum_rot_updown, 1, 0, 0)
            glMultMatrixf(self.current_mv_mat)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            for render in self.render:
                render.update()

            glPopMatrix()

            pygame.display.flip()
            pygame.time.wait(10)