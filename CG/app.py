import pygame
import threading
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Mouse:
    def __init__(self):
        self.pos = None
        self.left_button_down = None
        self.right_button_down = None
        self.left_button_up = None
        self.right_button_up = None
        self.left_button_activate = False
        self.right_button_activate = False

    def left_button_release(self):
        if not self.left_button_activate and self.left_button_down:
            self.left_button_activate = True
            return True

        elif self.left_button_activate and self.left_button_up:
            self.left_button_activate = False
            self.left_button_up = False

        return False
    
    def right_button_release(self):
        if not self.right_button_activate and self.right_button_down:
            self.right_button_activate = True
            return True
        
        elif self.right_button_activate and self.right_button_up:
            self.right_button_activate = False
            self.right_button_up = False

        return False

        
class Keyboard:
    def __init__(self):
        self.key_press = None

class App:
    def __init__(self):
        self.render = []
        self.speed = 3
        self.sum_rot_updown = 0
        self.current_mv_mat = (GLfloat * 16)()
        self.screenSize = (500, 500)
        self.mouse:Mouse = None
        self.keyboard:Keyboard = None


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
                elif event.type == pygame.MOUSEBUTTONUP and self.mouse:
                    if event.button == 1:
                        self.mouse.left_button_up = True
                    
                    if event.button == 3:
                        self.mouse.right_button_up = True

            if not self.mouse is None:
                self.mouse.pos = pygame.mouse.get_pos()
                self.mouse.left_button_down = pygame.mouse.get_pressed()[0]
                self.mouse.right_button_down = pygame.mouse.get_pressed()[2]
            
            if not self.keyboard is None:
                self.keyboard.key_press = pygame.key.get_pressed()

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

    def start_thread(self, target):
        th = threading.Thread(target=target)
        th.daemon = True
        th.start()