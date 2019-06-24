import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class oscillator:

    def __init__(self, mass, spring_c, step, sample_rate):

        # model variables
        self.m = mass
        self.D = spring_c
        self.h = step
        self.time = np.linspace(0, 100, sample_rate)
        self.curve_pos = np.zeros((len(self.time), 2))  # es gibt zu jedem zeitpunkt einen x und einen y eintrag.
        # curve_pos[t] ist abhängig von der zeit
        self.vel = np.asanyarray([0, 0])    # aktueller geschwindigkeitsvektor

        # plot variables
        matplotlib.use("TkAgg")                 # Komischer fix für ein komisches Problem
        self.fig, self.ax = plt.subplots()
        self.plot_objects = dict()

        amplitude = 0.2

        # anfangsgeschwindigkeit setzen
        init_vel = np.asarray([np.random.uniform(-amplitude, amplitude),
                               np.random.uniform(-amplitude, amplitude)])
        for coord in init_vel:
            if coord == 0:
                coord = 1

        self.vel = init_vel

        # positionen intitialisieren
        init_pos = np.asarray([np.random.uniform(-amplitude, amplitude),
                               np.random.uniform(-amplitude, amplitude)])
        for coord in init_pos:
            if coord == 0:
                coord = 1

        self.curve_pos[0] = init_pos

        for t in range(self.h, len(self.time)):
            self.curve_pos[t] = self.curve_pos[t - self.h] + self.vel * self.h
            self.vel += self.centripetal_a(self.curve_pos[t])
        print(self.curve_pos)

    def centripetal_a(self, pos):
        return (-self.D * pos) / self.m

    def ani_init(self):

        # define plot objects
        self.plot_objects['curve'], = self.ax.plot([], [], "-", color="blue")   # laufbahn
        self.plot_objects['origin'] = self.ax.plot(0, 0, "x", color="red")      # fixpunkt
        self.plot_objects['pos'], = self.ax.plot([], [], "o", color="black")    # aktuelle pos
        self.plot_objects['lin'], = self.ax.plot([], [], 'r-', linewidth=3)     # geschwindigkeit

        self.plot_objects['text'] = self.ax.text(0.1, 0.2, '', transform=self.ax.transAxes)

        # set data
        self.plot_objects['curve'].set_data(self.curve_pos.transpose()[0],
                                            self.curve_pos.transpose()[1])

        # initial place holder, data will be set in ani_step
        self.plot_objects['pos'].set_data([], [])
        self.plot_objects['text'].set_text('')
        self.plot_objects['lin'].set_data([], [])

        return self.plot_objects['pos'], self.plot_objects['text'], self.plot_objects['lin'],

    # animationsschritt
    def ani_step(self, t):

        self.plot_objects['pos'].set_data([self.curve_pos[t][0]], [self.curve_pos[t][1]])
        self.plot_objects['text'].set_text(str(t))
        tan = [self.curve_pos[t + 1][0] - self.curve_pos[t - 1][0], self.curve_pos[t + 1][1] - self.curve_pos[t - 1][1]]
        self.plot_objects['lin'].set_data([self.curve_pos[t][0] - tan[0], self.curve_pos[t][0] + tan[0]],
                                          [self.curve_pos[t][1] - tan[1], self.curve_pos[t][1] + tan[1]])

        return self.plot_objects['pos'], self.plot_objects['text'], self.plot_objects['lin']

    # animation
    def paint(self):
        ani = animation.FuncAnimation(self.fig, self.ani_step, np.arange(1, len(self.time)),
                                      interval=50, blit=True, init_func=self.ani_init)

        # Rand auf plot zuschneiden
        max = np.nanmax(self.curve_pos.transpose(), 1)
        self.ax.set_xlim((-1 * max[0] * 11) / 10, (11 * max[0]) / 10)
        self.ax.set_ylim(-1 * max[1] * 11 / 10, max[1] * 11 / 10)
        plt.show()


if __name__ == '__main__':
    test = oscillator(6, 0.1, 1, 10000)
    test.paint()
