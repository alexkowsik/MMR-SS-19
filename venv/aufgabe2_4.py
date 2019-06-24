import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class celestial_body:

    def __init__(self, name, mass):
        self.name = name
        self.m = mass
        self.pos = tuple([0, 0])    # [0] = x, [1] = y

    def __str__(self):
        print(self.name + ' is at: ' + str(self.pos))


class planet(celestial_body):

    def __init__(self, name, sun, mass, distance_to_sun, rotational_speed, sample_rate):
        super(celestial_body, self).__init__(name, mass)    # TODO: weiß nich ob das so geht, sollte aber passen
        self.sun = sun
        self.rad = distance_to_sun
        self.pos = tuple([0, distance_to_sun])
        self.vel = tuple([rotational_speed, 0])     # [0] = x, [1] = y
        self.curve = np.zeros(sample_rate, 2)



class simulation:

    def __init__(self, mass, spring_c, step, sample_rate):

        # model variables
        self.h = step
        self.time = np.linspace(0, 100, sample_rate)

        # initialize planets
        sun = celestial_body('sun', 1988500e24)
        planets = []
        mercury = planet('mercury', sun, 0.330e24, 57.9e9, 47.4e3, sample_rate)
        planets.append(mercury)
        venus = planet('venus', sun, 4.87e24, 108.2e9, 35e3, sample_rate)
        planets.append(venus)
        earth = planet('earth', sun, 5.97e24, 149.6e9, 29.8e3, sample_rate)
        planets.append(earth)
        mars = planet('mars', sun, 0.642e24, 227.9e9, 24.1e3, sample_rate)
        planets.append(mars)
        jupiter = planet('jupiter', sun, 1898e24, 778.6e9, 13.1e3, sample_rate)
        planets.append(jupiter)


        # plot variables
        matplotlib.use("TkAgg")                 # Komischer fix für ein komisches Problem
        self.fig, self.ax = plt.subplots()
        self.plot_objects = dict()

        for t in range(self.h, len(self.time)):
            self.curve_pos[t] = self.curve_pos[t - self.h] + self.vel * self.h
            self.vel += self.centripetal_a(self.curve_pos[t])

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
        self.plot_objects['lin'].set_data([self.curve_pos[t][0], self.curve_pos[t][0] + tan[0]],
                                          [self.curve_pos[t][1], self.curve_pos[t][1] + tan[1]])

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
    test = simulation(6, 0.1, 1, 10000)
    test.paint()
