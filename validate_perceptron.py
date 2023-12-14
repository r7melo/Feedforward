import json

from Perceptron import Perceptron

def load_perceptrons():
    try:
        with open('perceptrons.json', 'r') as file:
            data = json.load(file)
            return [Perceptron(p["bias"], p["w"]) for p in data]
    except FileNotFoundError:
        return [] 

# Lista de pessoas
ps = load_perceptrons()

p = ps[0]

data = [[1,1,1],[1,0,0],[0,1,0],[0,0,0],[0,2,1]]

for i in data:
    p.input(i[:2])
    S = p.output()
    y = p.activate(S)
    print(f"{i} y={y}")