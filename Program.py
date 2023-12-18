from OpenGL.GL import *
import threading
import pygame
from Perceptron import Perceptron
from CG import App, Mouse, Keyboard, CartesianPlane


class Program:
    def __init__(self):
        self.mouse:Mouse
        self.keyboard:Keyboard

    def start_mouse(self):
        while True:
            
            if self.mouse.left_button: 
                print(f"left={self.mouse.pos}")

            if self.mouse.right_button: 
                print(f"rigth={self.mouse.pos}")


    def start_keyboard(self):
        while True:

            if self.keyboard.key_press and self.keyboard.key_press[pygame.K_ESCAPE]:
                print("ESCAPE")




if __name__=="__main__":
    
    app = App()
    app.screenSize = (500, 500)
    app.render.append(CartesianPlane())

    program = Program()
    program.mouse = Mouse()
    program.keyboard = Keyboard()

    app.mouse = program.mouse
    app.keyboard = program.keyboard
    app.start_thread(program.start_mouse)
    app.start_thread(program.start_keyboard)

    app.run()