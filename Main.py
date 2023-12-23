import json
import pygame
from OpenGL.GL import *
from CG import App
from network_neural import NetworkNeural





class Program:
    def __init__(self):
        self.network_neural:NetworkNeural


    def mouse_button_up(self, event):
        if event.button == 1:
            print(f"Left: {event.pos}")
        elif event.button == 3:
            print(f"Right: {event.pos}")

    def save_perceptrons(self):
        with open('modelo.json', 'w') as arquivo:
            pJson = []
            json.dump(pJson, arquivo)
            print("salvo!")



if __name__=="__main__":
    
    app = App()
    app.screenSize = (500, 500)

    

    program = Program()
    program.network_neural = NetworkNeural([2,2,1])

    app.event_actions[pygame.MOUSEBUTTONUP] = [program.mouse_button_up]
    app.start_thread(program.save_perceptrons, delay=10)

    app.run()