import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, floor
"""
Zur Theoriefrage:
"""


# Aufgabe1
def teila():
    # Verwendetes Polynom : (x(^3)/200)+2(^-3)(x^2)
    # IN dem Code fitte ich ein Polynom und werte es an (30+15)*h Stellen aus,
    # d.h. mache ein Gitter mit Paaren (x,f(x)) mit Abstand h zwischen den X-Werten jedes Paars.
    # Um die Ableitung zu bestimmten, muss man also 2 benachbarte Elemente des
    # Arrays mit den ausgewerteten Stellen f(x) in die Formel einsetzen.
    # Die Formel mit 1/h ist in dem Programm zu verwenden, indem man
    # die Variable 'alternativ' auf := False setzt.

    # Zur Zusatzfrage: In der Praxis kann das h nur endlich nah an 0 angenähert werden.
    # Es lässt sich also ein Polynom finden, dass an Stelle f(x) = a , f(x+h) = a+negl(h)
    # und f(x-h) = b, wobei a,b beliebig (also auch ganz weit auseinander) und negl(h) eine
    # vernachlässigbare Funktion. In der Theorie lässt sich kein solches Polynom finden, weil man
    # h beliebig klein machen kann.

    # Je größer h ist, desto mehr weicht die Ableitung von der tatsächlichen ab.
    # Je kleiner, desto näher an der tatsächlichen Ableitung (und rechenaufwendiger)
    # Für das gefundene Polynom stürzt das Programm für h>7 ab. oops.
    # Man kann es aber seeehr klein machen. h = 0.001 ist recht schnell.

    # Die alternative Methode ist recht genau für h~1, aber für niedrigere h ist die Ableitung
    # eine horizontale Gerade(vlt weil die Änderung der Funktion sehr klein wird, je kleiner
    # h ist) und für h>1 wird das Programm sehr ungenau ( Abstand der Punkte zu groß)

    plt.style.use('seaborn-whitegrid')
    h = 2            # h einstellen
    p = np.poly1d([1/200, 2**-3, 0, 0])
    # Das Polynom in einem h-feinen Gitter von -30 bis 15 ausgewertet
    # wenn man hier die Grenzen für x ändert, muss man es auch unten bei den Plots/HP/TP tun
    poly = np.vectorize(p)(np.arange(-30, 15, h))

    # Berechnet  hier die Ableitungen mit der ausgewählten Methode
    deriv = np.zeros(poly.shape[0]-1)
    alternativ = False             # zum Auswählen der Methode

    if alternativ:
        # Man bekommt keine Ableitung an der ersten und letzten Stelle x
        for i in range(1, poly.shape[0]-1):
            deriv[i] = (poly[i+1]-poly[i-1])/2*h
    else:
        # Man bekommt keine Ableitung an der letzten Stelle x
        for i in range(poly.shape[0] - 1):
            deriv[i] = (poly[i + 1] - poly[i]) / h


    #plot für Das Polynom an sich
    ax1 = plt.subplot()
    ax1.plot(np.arange(-30,15,h),poly, 'r-', label = 'funkt')
    ax1.set_ylim(-15, 25)

    # Plot für die numerische Ableitung
    ax2 = ax1.twinx()
    ax2.plot(np.arange(-30, 15, h)[alternativ:-1], deriv[alternativ:],  'b-.', label = 'num. Abl')
    ax2.set_ylim(-15, 25)

    # Plot für die symbolische Ableitung, von numpy berchnet
    ax3 = ax1.twinx()
    ax3.plot(np.arange(-30, 15, h), np.vectorize(p.deriv())(np.arange(-30, 15, h)), 'y--', ms = 15, label = 'symb.Abl')
    ax3.set_ylim(-15, 25)

    # Plot für die symblische Ableitung, selbst berechnet, das selbe wie was numpy macht
    # ax4 = ax1.twinx()
    # ax4.plot(np.arange(-30, 15, h),np.vectorize(np.poly1d([3/200, 2**-2, 0]))(np.arange(-30, 15, h)), 'y--', ms = 15, label = 'symb.Abl')
    # ax4.set_ylim(-15, 25)

    # um die Extrema zu berechnen iteriere durch die Ableitung, speichere jede Stelle Mit VZwechsel,
    # und den Wert des Polynoms an dieser Stelle in ein Array. Suche dann das Maximum(HP)
    # bzw Minimum(TP) für den Wert des Polynoms und plotte an diese Stelle entsprechende Punkte

    if alternativ:
        prev = deriv[1]
    else:
        prev = deriv[0]

    HP = []
    TP = []
    for i in range(1+alternativ, deriv.shape[0]-1):
        next = deriv[i]
        if next != 0:
            if prev < 0 < next:
                # plt.plot(np.arange(-20, x_limiter, h)[alternativ + i], [ycoords[i]], 'g.', ms = 20)
                TP.append((poly[i], i))

            if prev > 0 > next:
                # plt.plot(np.arange(-20, x_limiter, h)[alternativ + i], [ycoords[i]], 'c.', ms = 20)
                HP.append((poly[i], i))

            prev = next
    max = HP[0]
    for thing in HP:
        if thing[0] > max[0]:
            max = thing
    plt.plot(np.arange(-30, 15, h)[alternativ + max[1]], [poly[max[1]]], 'c.', ms=20)

    max = TP[0]
    for thing in TP:
        if thing[0] < max[0]:
            max = thing
    plt.plot(np.arange(-30, 15, h)[alternativ + max[1]], [poly[max[1]]], 'g.', ms=20)

    plt.show()


def teilapraxis():
    # benutze hier einfach den Code aus dem 1. Teil für Sin und Cos

    # die num. Ableitung von sin(1/x) ist von der Form her ähnlich zu der symbolischen Abl,
    # aber um 1 nach unten verschoben. Es scheint, dass f(x+h)-f(x) ungefähr Null ist, dh sich
    # nicht viel zwischen den Ableitungverfahren unterscheidet.

    x = False   # Variable zur Auswahl von x oder 1/x als Argument für den Sinus
    alternativ = False

    plt.style.use('seaborn-whitegrid')
    h = 0.05
    xcoords = np.arange(-10, 10, h)     # es reicht hier die grenzen von x zu ändern!

    if x:       # sin(x)
        ycoords = np.vectorize(sin)(xcoords)
    else:       # sin(1/x)
        xcoords = np.delete(xcoords, np.where(xcoords == 0), axis = 0)
        ycoords = np.vectorize(sin)(1/xcoords)

    deriv = np.zeros(ycoords.shape[0] - 1)

    if alternativ:
        for i in range(1, ycoords.shape[0] - 1):
            deriv[i] = (ycoords[i + 1] - ycoords[i - 1]) / 2 * h
    else:
        for i in range(ycoords.shape[0] - 1):
            deriv[i] = (ycoords[i + 1] - ycoords[i]) / h

    ax1 = plt.subplot()
    ax1.plot(xcoords, ycoords, 'r-', label='funkt')
    ax1.set_ylim(-1, 1)

    ax2 = ax1.twinx()
    ax2.plot(xcoords[alternativ:-1], deriv[alternativ:], 'b-.', label='num. Abl')
    ax2.set_ylim(-1, 1)

    ax3 = ax1.twinx()
    if x:       # plot sin(x)
        ax3.plot(xcoords, np.vectorize(cos)(xcoords), 'y--', ms=15, label='symb.Abl')
    else:       # plot sin(1/x)
        ax3.plot(xcoords, np.vectorize(cos)(1/xcoords), 'y--', ms=15, label='symb.Abl')
    ax3.set_ylim(-1, 1)

    plt.text(-10, 1, "Rote Linie: Funktion\nBlaue Linie: num Abl\nGelbe Linie: Symb. Abl", fontsize=12)
    plt.show()


def teilb():
    # Was hier Passiert: man trägt die messwerte auf und berechnet die ableitung wie in teil a.
    # für h <1 ist die ableitung fast eine gerade und für große h > 1 schwankt sie stark und ist schwer leserlich.
    # das leigt daran, dass die messdaten an sich stark schwanken
    # Extremstellen erkennen funktionieren aber gut

    #Erstelle Polynpom aus Messwerten an points-to-evaluate vielen STellen
    plt.style.use('seaborn-whitegrid')
    x_limiter = 520     #bis zu welchem Punk tim DAtensatz man auswerten möchte
    measurements = np.loadtxt("measurements.txt", skiprows=3)  # skippe header
    poits_to_evaluate = 500  # anzahl der punkte die man plotten/evaluaten möchte
    xa = np.linspace(0, poits_to_evaluate - 1, poits_to_evaluate)  # x-coords
    ya = np.array(measurements[0:poits_to_evaluate, 6])  # y-werte an x-coords
    coeff = np.polyfit(xa, ya, 4)  # erstellt ein polynom aus den messwerten

    #Benutze hier das Polynom der Messwerte um die Ableitung zu berechnen
    p = np.poly1d(coeff)
    h = 1
    xcoords = np.arange(-20, x_limiter, h)
    ycoords = np.vectorize(p)(xcoords)


    interval = 10 * x_limiter + 1
    ylim_for_plots = [-20, 100]
    xlim_for_plots = [-20, x_limiter]
    x = np.linspace(-20, x_limiter, interval)
    b = np.linspace(0, measurements.shape[0] - 1, 6)  # stützstellen

    temp = []
    for i in b:
        temp.append(measurements[floor(i), 6])
    y = np.asarray(temp)

    temp = []
    for i in range(len(b)):
        temp.append(np.ones(interval))
    l_vectors = np.asarray(temp)
    for k in range(len(l_vectors)):
        for i in range(interval):
            for j in range(len(b)):
                if j != k:
                    l_vectors[k][i] *= (x[i] - b[j]) / (b[k] - b[j])

    for i in range(len(l_vectors)):
        l_vectors[i] *= y[i]

    reduced = np.add.reduce(l_vectors)

    derive = np.zeros(ya.shape[0] - 1)

    alternativ = True
    if (alternativ):
        for i in range(1, ya.shape[0] - 1):
            derive[i] = (ya[i + 1] - ya[i - 1]) / 2 * h
    else:
        for i in range(ycoords.shape[0] - 1):
            derive[i] = (ya[i + 1] - ya[i]) / h

#poly interpolation
    subp1 = plt.subplot()
    subp1.set_xlim(xlim_for_plots)
    subp1.set_ylim(ylim_for_plots)
    subp1.plot(xa, ya, 'b-')        #x,reduced

#num derviation
    subp3 = subp1.twinx()
    subp3.plot(xa[alternativ:-1],derive[alternativ:], 'y-.')
    subp3.set_ylim(ylim_for_plots)
    subp3.set_xlim(xlim_for_plots)
#polyfit
    subp2 = subp1.twinx()
    subp2.plot(xcoords,ycoords, 'r-', markersize=6)
    subp2.set_ylim(ylim_for_plots)
    subp2.set_xlim(xlim_for_plots)
#polyfits derivation
    subp4 = subp1.twinx()
    #subp4.plot(xcoords, np.vectorize(p.deriv())(xcoords), 'g-', markersize=6)
    subp4.set_ylim(ylim_for_plots)
    subp4.set_xlim(xlim_for_plots)


#HP/TP
    if alternativ:
        prev = derive[1]
    else:
        prev = derive[0]

    HP = []
    TP = []
    for i in range(1+alternativ,derive.shape[0]-1):
        next = derive[i]
        if next != 0:
            if (prev < 0 and next > 0):
                TP.append((ya[i], i))

            if (prev > 0 and next < 0):
                HP.append((ya[i], i))

            prev = next
    max = HP[0]
    for thing in HP:
        if thing[0] > max[0]:
            max = thing

    plt.plot(xa[alternativ + max[1]], [ya[max[1]]], 'c.', ms=20)

    max = TP[0]
    for thing in TP:
        if thing[0] < max[0]:
            max = thing

    plt.text(-20, ylim_for_plots[1], "Rote Linie: Funktion durch polyfit \nGelbe Linie: num Abl"
                                     "\nBlaue Liie: Messwerte", fontsize=12)
    plt.plot(xa[alternativ + max[1]], [ya[max[1]]], 'g.', ms=20)

    plt.show()


def approxAbl():

    #das ist der modifizierte code aus woche 2. Berechne hier MLS mit polyfit
    # und gleichzeitig die ableitung mittels der derive() -funktion von poly1d
    # diese berechnet die ableitug von dem geftitteten polynom.
    # die berechnung findet in der for schleife mit dem fenster statt, an dieser stelle
    # unterscheidet sich der code von dem , was wir zu week 2 gemacht haben
    # die ableitung lässt sich aber auch so berechnen: man multipliziert das i-te element mit i
    # im ganzen array und dann verschiebt man das i-te element an die (i-1)-te
    # Stelle im array, wobei man von rechts anfängt(damit keine elemente überschrieben
    # werden) und das element ganz rechts ion der liste fällt weg, die liste wird um 1
    # element kürzer. Beim Ableiten werden ja alle koeffizienten mit der potenz multipliziert
    # und die Potenz wird um1  kleiner
    plt.style.use('seaborn-whitegrid')
    measurements = np.loadtxt("measurements.txt", skiprows=3)  # skippe header
    x = measurements[:, 6]  # Temperatur-Daten

    # Temp plotten
    x_coords = np.arange(0, x.shape[0])

    ax1 = plt.subplot()
    ax1.plot(x_coords, x, 'r.')
    ax1.set_xlabel('Zeitpunkt')
    ax1.set_ylabel('Temp', color='r')



    # In Step die Größe des Fensters einstellen
    mls = np.zeros(x.shape[0])
    h = 60
    x_coordsA = np.zeros(x.shape[0])
    deriv = np.zeros(x.shape[0])

    for i in range(x.shape[0] - h):
        x_coordsA[i] = i + h / 2
        coeff = np.polyfit(x_coords[i:i+h], x[i:i+h], 5)
        p = np.poly1d(coeff)
        #berechne hier die ableitung auf die faule art und weise
        q = np.poly1d(coeff).deriv()
        mls[i] = p(x_coordsA[i])
        deriv[i] = q(x_coordsA[i])

    ax1.plot(x_coordsA[:-h], mls[:-h], color="y")

    ax2 = plt.subplot()
    ax2.plot(x_coordsA[:-h], deriv[:-h], 'm-')
    ax2.set_xlabel('Zeitpunkt')
    ax2.set_ylabel('num. Ableitung', color='y')

    # HP/TP
    prev = deriv[0]
    HP = []
    TP = []
    for i in range(1 , deriv.shape[0] - 1):
        next = deriv[i]
        if next != 0:
            if (prev < 0 and next > 0):
                TP.append((mls[i], i))

            if (prev > 0 and next < 0):
                HP.append((mls[i], i))

            prev = next

    max = HP[0]
    for thing in HP:
        if thing[0] > max[0]:
            max = thing

    plt.plot(x_coordsA[max[1]], [mls[max[1]]], 'c.', ms=20)

    max = TP[0]
    for thing in TP:
        if thing[0] < max[0]:
            max = thing
    plt.plot(x_coordsA[max[1]], [mls[max[1]]], 'g.', ms=20)


    plt.show()


#unterschiedliche h: immer genauer an errechneter Ableitung, aber immer noh versetzt
#alternative def: linke seite hebt vom errechneten wert genauso wie die rechte ab
if __name__=="__main__":
    teilb()
