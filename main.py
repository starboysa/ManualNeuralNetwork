import matplotlib.pyplot as plt
import random
import tkinter as tk
from math import *

random.seed()

class NN:
    
    def __init__(self):
        self.hiddenLayerCount = 30

        self.weights = []
        for i in range(0, self.hiddenLayerCount + 1):
            self.weights.append(random.random())

    def train(self, xHats, yHats):
        for itr in range(0, 10000):
            root.update()
            
            o = []
            for x in xHats:
                o.append(self.out(x))

            E = 0
            for i in range(0, len(yHats)):
                E += (o[i] - yHats[i])**2

            # Normal weights
            for j in range(0, self.hiddenLayerCount):

                sm = 0
                for i in range(0, len(yHats)):
                    sm += (o[i] - yHats[i]) * self.activation(xHats[i] - (j / self.hiddenLayerCount))

                sm *= 2
                
                self.weights[j] = self.weights[j] - 0.003 * sm

            # w0 weight
            sm = 0
            for i in range(0, len(yHats)):
                sm += o[i] - yHats[i]

            sm *= 2
            self.weights[self.hiddenLayerCount] = self.weights[self.hiddenLayerCount] - 0.003 * sm

            errLabel.config(text=E)
            itrLabel.config(text=itr)

            if E < 0.001:
                return
        
    
    def out(self, x):
        sm = 0
        for i in range(0, self.hiddenLayerCount):
            sm += self.weights[i] * self.activation(x - (i / self.hiddenLayerCount))

        sm += self.weights[self.hiddenLayerCount]

        return sm

    def activation(self, x):
        if (x > 0):
            return x
        else:
            return 0


def assignment():
    b.config(state=tk.DISABLED)
    network = NN()

    xTraining = []
    yTraining = []
    for i in range(0, 50):
        num = i / 50
        xTraining.append(num)

        x = num
        yTraining.append(eval(str(v.get())))

    network.train(xTraining, yTraining)
    b.config(state=tk.NORMAL)

    xValues = []
    yValues = []
    for i in range(0, 50):
        num = i / 50
        xValues.append(num)
        yValues.append(network.out(num))

    plt.yscale("linear")
    plt.ylim([-1.5, 1.5])

    plt.plot(xTraining, yTraining, label='Training Data')
    plt.plot(xValues, yValues, label='NN Output')
    plt.legend()
    plt.show()

root = tk.Tk();
root.title("Manual Neural Network")
l = tk.Label(root, text="Function")
l.grid(row=0)

v = tk.StringVar(root, value='sin(2 * pi * x)')
e1 = tk.Entry(root, textvariable=v)
e1.grid(row = 0, column = 1)

b = tk.Button(root, text="Start Training", width=25, command=assignment)
b.grid(row=1)

errorTextLabel = tk.Label(root, text="Error (0.001 min): ")
errorTextLabel.grid(row=2)

errLabel = tk.Label(root, text="", anchor="w", width=30)
errLabel.grid(row=2, column=1);

iterationTextLabel = tk.Label(root, text="Iteration (out of 10000):")
iterationTextLabel.grid(row=3)

itrLabel = tk.Label(root, text="", anchor="w", width=30)
itrLabel.grid(row=3, column=1)

root.mainloop()
