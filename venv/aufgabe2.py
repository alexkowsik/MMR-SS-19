import numpy as np
import matplotlib;

matplotlib.use("TkAgg")  # Komischer fix für ein komisches Problem
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Das ist der Plot für die Laufbahn. Wir später erst von curve_pos befüllt
curve, = ax.plot([], [], "-", color="blue")

# da wir um einen Punkit rotieren, malen wir uns diesen hier
origin = ax.plot(0, 0, "x", color="red")

# pos ist die aktuelle Position auf der Bahn beschrieben in curve_pos.
# d.h. pos ist curve[t][0] und curve[t][1] und diese punkte malen wir immer neu ( t ist die zeit)
pos, = ax.plot([], [], "o", color="black")
text = ax.text(0.1, 0.2, '', transform=ax.transAxes)
# line für die Geswchwindigkeit
lin, = ax.plot([], [], 'r-', linewidth=3)

# berechnnung der neuen position

mass = 6  # masse des pendels
D = 0.1  # federkonstante
h = 1  # Schrittweite(tick)
time = np.linspace(0, 100, 10000)  # Zeitgitter


def F(pos):  # Rückstellkräfte
    global D, mass
    return (-D * pos) / mass


# Zufällige startpositionen/-geschwindigkeiten
x_init = np.asarray([np.random.uniform(-1, 1),
                     np.random.uniform(-1, 1)])
for item in x_init:
    if item == 0:
        item = 1

x_deriv = np.asarray([np.random.uniform(-1, 1),
                      np.random.uniform(-1, 1)])
for item in x_deriv:
    if item == 0:
        item = 1

curve_pos = np.zeros((len(time), 2))  # es gibt zu jedem zeitpunkt einen x und einen y eintrag
curve_pos[0] = x_init  # pos[t] ist abhängig von der zeit

# Berechner hier die Position des Pendels für Zeit t durch : Position an Zeit t-1 + Geschwindigkeit
# an Zeit t-1

for t in range(1, len(time)):
    curve_pos[t] = curve_pos[t - h] + x_deriv * h
    x_deriv += F(curve_pos[t])


# initialisierung der animation (startbild)
def init():
    curve.set_data(curve_pos.transpose()[0],
                   curve_pos.transpose()[1])
    pos.set_data([], [])
    text.set_text('')
    lin.set_data([], [])
    return pos, text, lin,


# ([curve_pos[t][0]-tan[0], tan*2],
#                  [curve_pos[t][1]-tan[1], tan*2])
# animationsschritt
def step(t):
    pos.set_data([curve_pos[t][0]], [curve_pos[t][1]])
    text.set_text(str(t))
    tan = [curve_pos[t + 1][0] - curve_pos[t - 1][0], curve_pos[t + 1][1] - curve_pos[t - 1][1]]
    lin.set_data([curve_pos[t][0] - tan[0], curve_pos[t][0] + tan[0]],
                 [curve_pos[t][1] - tan[1], curve_pos[t][1] + tan[1]])

    return pos, text, lin


# np.arange gibt uns ein array von 1,2,...,(länge des arrays mit den x-Werten)
ani = animation.FuncAnimation(fig, step, np.arange(1, len(time)),
                              interval=50, blit=True, init_func=init)

max = np.nanmax(curve_pos.transpose(), 1)
ax.set_xlim((-1 * max[0] * 11) / 10, (11 * max[0]) / 10)
ax.set_ylim(-1 * max[1] * 11 / 10, max[1] * 11 / 10)
plt.show()
