import pygame
import threading
import time

# Inicialização do Pygame
pygame.init()

# Variável compartilhada para sincronização entre as threads
lock = threading.Lock()

# Definição de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dimensões da janela
WIDTH, HEIGHT = 400, 400

# Criação da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Line Drawing")

def draw_line1():
    with lock:
        pygame.draw.line(screen, WHITE, (50, 50), (350, 350), 2)
        pygame.display.flip()

def draw_line2():
    with lock:
        pygame.draw.line(screen, WHITE, (50, 350), (350, 50), 2)
        pygame.display.flip()

def draw_lines_in_parallel():
    # Inicia as threads para desenhar as linhas
    drawing_thread1 = threading.Thread(target=draw_line1)
    drawing_thread2 = threading.Thread(target=draw_line2)

    drawing_thread1.start()
    drawing_thread2.start()

    # Aguarde ambas as threads terminarem antes de encerrar o programa
    drawing_thread1.join()
    drawing_thread2.join()

if __name__ == "__main__":
    # Inicia as threads de desenho
    draw_lines_in_parallel()

    # Aguarda um pouco antes de fechar a janela
    time.sleep(2)

    # Encerra o Pygame
    pygame.quit()
