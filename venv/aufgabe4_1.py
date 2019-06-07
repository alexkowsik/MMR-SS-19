import numpy as np
import matplotlib.pyplot as plt
from math import sin,cos,floor
"""
Zur Theoriefrage:
"""
#Verwendetes Polynom : (x(^3)/200)+2(^-3)(x^2)

#Aufgabe1
def teila():
    plt.style.use('seaborn-whitegrid')
    h =1
    p = np.poly1d([1/200,2**-3,0,0])
    poly = np.vectorize(p)(np.arange(-30,15,h))
    deriv = np.zeros(poly.shape[0]-1)
    alternativ  = False
    if(alternativ):
        for i in range(1,poly.shape[0]-1):
            deriv[i]= (poly[i+1]-poly[i-1])/2*h
    else:
        for i in range(poly.shape[0] - 1):
            deriv[i] = (poly[i + 1] - poly[i]) / h

    ax1 = plt.subplot()
    ax1.plot(np.arange(-30,15,h),poly, 'r-', label = 'funkt')
    ax1.set_ylim(-15, 25)

    ax2 = ax1.twinx()
    ax2.plot(np.arange(-30,15,h)[alternativ:-1],deriv[alternativ:],  'b-.',label = 'num. Abl')
    ax2.set_ylim(-15,25)

    ax3 = ax1.twinx()
    ax3.plot(np.arange(-30,15,h),np.vectorize(p.deriv())(np.arange(-30,15,h)),'y--',ms = 15,label = 'symb.Abl')
    ax3.set_ylim(-15, 25)

    #ax4 = ax1.twinx()
    #ax4.plot(np.arange(-30,15,h),np.vectorize(np.poly1d([3/200,2**-2,0]))(np.arange(-30,15,h)),'y--',ms = 15,label = 'symb.Abl')
    #ax4.set_ylim(-15, 25)

    if alternativ:
        prev = deriv[1]
    else:
        prev = deriv[0]
    next = 0
    for i in range(1+alternativ,deriv.shape[0]-1):
        next = deriv[i]
        if next != 0:
            if (prev < 0 and next > 0):
                plt.plot(np.arange(-30, 15, h)[1 + alternativ + i], [prev], 'g.',ms = 20)

            if (prev > 0 and next < 0):
                plt.plot(np.arange(-30, 15, h)[1 + alternativ + i], [prev], 'c.',ms = 20)

            prev = next
    plt.text(-32,17,"Cyan Punkt: HP\nGreen Punkt: TP\n"
                    "Rote Linie: Funktion\nBlaue Linie: num Abl"
                "\nGelbe Linie: Symb. Abl",fontsize = 12)
    plt.show()

def teilapraxis():
    plt.style.use('seaborn-whitegrid')
    h = 0.01
    xcoords = np.arange(-10,10,h)
    #wenn sin(1/x)
    xcoords = np.delete(xcoords,np.where(xcoords == 0),axis = 0)
    ycoords = np.vectorize(sin)(1/xcoords)

    deriv = np.zeros(ycoords.shape[0] - 1)
    alternativ = False
    if (alternativ):
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
    ax2.set_ylim(-1,1)

    ax3 = ax1.twinx()
    ax3.plot(xcoords, np.vectorize(cos)(1/xcoords), 'y--', ms=15, label='symb.Abl')
    ax3.set_ylim(-1, 1)

    plt.text(-10,1, "Rote Linie: Funktion\nBlaue Linie: num Abl"
                      "\nGelbe Linie: Symb. Abl", fontsize=12)
    plt.show()

def teilb():
    measurements = np.loadtxt("measurements.txt", skiprows=3)  # skippe header

    x_limiter = 520
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
    h = 0.01
    xcoords = np.arange(-20, x_limiter, h)
    derive = np.zeros(reduced.shape[0] - 1)
    alternativ = True
    if (alternativ):
        for i in range(1, reduced.shape[0] - 1):
            derive[i] = (reduced[i + 1] - reduced[i - 1]) / 2 * h
    else:
        for i in range(reduced.shape[0] - 1):
            derive[i] = (reduced[i + 1] - reduced[i]) / h


    subp1 = plt.subplot()
    subp1.set_xlim(xlim_for_plots)
    subp1.set_ylim(ylim_for_plots)
    subp1.plot(x, reduced, 'b-')

#new plot
    subp3 = subp1.twinx()
    subp3.plot(derive,x[:-1], 'y-.')
    subp3.set_ylim(ylim_for_plots)
    subp3.set_xlim(xlim_for_plots)
#end plot
    subp2 = subp1.twinx()
    subp2.plot(b, y, 'r.', markersize=12)
    subp2.set_ylim(ylim_for_plots)
    subp2.set_xlim(xlim_for_plots)


    plt.show()


    plt.show()
#unterschiedliche h: immer genauer an errechneter Ableitung, aber immer noh versetzt
#alternative def: linke seite hebt vom errechneten wert genauso wie die rechte ab
if __name__=="__main__":
    teilb()