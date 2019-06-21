import numpy as np
import matplotlib
from math import radians

matplotlib.use("TkAgg")  # Komischer fix für ein komisches Problem
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

originPoint = [0, 0]
origin = ax.plot(0, 0, "x", color="red")
pos, = ax.plot([], [], "o", color="black")
text = ax.text(0.1, 0.2, '', transform=ax.transAxes)
lin, = ax.plot([], [], 'r-', linewidth=3)

l = 2 # Seillänge
h = 1 # Schrittweite
c = 0.95 # Dämpfungskonstante
time = np.linspace(0, 100, 1000)

# Zufällige startauslenkung/-Geschwindigkeit
init_alpha = 0
init_alphaDeriv = np.random.uniform(-20, 20)

# In alpha stehen die Auslenkungen, in alphaDeriv die Ableitungen davon
alpha = np.zeros(len(time))
alpha[0] = init_alpha
alphaDeriv = np.zeros(len(time))
alphaDeriv[0] = init_alphaDeriv


# Berechne zweite Ableitung wie vorgegeben
def get2ndDeriv(pos):
    global l
    return (-9.81 / l) * np.sin(radians(pos))


# Berechnen der Auslenkungen und der Ableitungen gleichzeitig, da man beides braucht
for t in range(h, len(time)):
    alpha[t] = (alpha[t - h] + alphaDeriv[t - h] * h)
    alphaDeriv[t] = (alphaDeriv[t - h] + get2ndDeriv(alpha[t]) * h) * c


def init():
    pos.set_data([], [])
    text.set_text('')
    lin.set_data([], [])
    return pos, text, lin,


# animationsschritt
def step(t):
    global l

    # In pos steht die Position des Kopfes berechnet aus den Auslekungen (ins Bogenmaß umgewandelt)
    pos.set_data([np.cos(radians(alpha[t] - 90)) * l], [np.sin(radians(alpha[t] - 90)) * l])
    text.set_text(str(t))
    lin.set_data([originPoint[0], np.cos(radians(alpha[t] - 90)) * l], [originPoint[1], np.sin(radians(alpha[t] - 90)) * l])

    return pos, text, lin

ani = animation.FuncAnimation(fig, step, np.arange(1, len(time)), interval=50, blit=True, init_func=init)

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
plt.show()
