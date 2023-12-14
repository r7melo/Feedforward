import time
import threading


class MinhaClasse:
    def __init__(self):
        self.variavel = 0

    def loop(self):
        while True:
            self.variavel += 1
            time.sleep(0.1)

    def clear(self):
        while True:
            if self.variavel > 100:
                self.variavel = 0


if __name__ == "__main__":
    minha_classe = MinhaClasse()

    thread = threading.Thread(target=minha_classe.loop)
    thread.daemon = True
    thread.start()

    # thread2 = threading.Thread(target=minha_classe.clear)
    # thread2.daemon = True
    # thread2.start()

    while True:
        print(minha_classe.variavel)
        time.sleep(1)

