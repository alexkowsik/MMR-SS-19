import matplotlib.pyplot as plt
from PIL import Image
import numpy as np



def aufgabe1():
    #hier stimmt iregndwas nicht.

    #ausgelegt auf bilder mit gleicher höhe wie breite

    #lädt bild in graustufen
    image = Image.open("../resources/pic2.jpg").convert("L")
    #image = Image.open("../resources/widepic.jpg").convert("L")

    img = np.asarray(image)
    print(img.shape)

#berechne hier die ableitungen, indem man zeilenweise
    h = 1
    x_dif = np.zeros(img.shape)
    y_dif = np.zeros(img.shape)
    grad = np.zeros((img.shape[0], img.shape[1], 2))

    # berechne hier die ableitung für x, indem man zeilenweise die ableitung
    # von 2h-weit entfernten punkten berechnet
    for y in range(img.shape[0]):
        for x in range(1,img.shape[1]-1):
            x_dif[y][x] = (img[y][x+h] - img[y][x-h])/2*h

    # berechne hier die ableitung für y, indem man spaltenweise die ableitung
    # von 2h-weit entfernten punkten berechnet
    for x in range(img.shape[1]):
        for y in range(1,img.shape[0]-1):
            y_dif[y][x] = (img[y+h][x] - img[y-h][x])/2*h

    # berechne gradientenvektor, der hat an jeder stelle ((s,y)-koordinate)
    # einen Vektor mit 2 einträgen stehen, nämlich der
    # (Ableitung von x, Ableitung von y) an den Koordinaten (x,y)
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            grad[y][x][0]= x_dif[y][x]
            grad[y][x][1] = y_dif[y][x]

    #print(x_dif[55][55],"hi",y_dif[55][55],"bbb",grad[55][55])

    fig, ax = plt.subplots()
    #berechne hier die pfeile zwischen d (x,y) und deren Ableitungen (Gradient)

    for y in range(0,img.shape[0],10):
        for x in range(0,img.shape[1],10):
            ax.arrow(y,x,grad[y][x][1],grad[y][x][0],fc="k", ec="k",
           head_width=5, head_length=5)
            print(y,x)

    #ax.arrow(55,55, grad [55][55][1], grad [55][55][0], fc="k", ec="k",
    #       head_width=15, head_length=15)

    #plotte bild
    ax.imshow(img, cmap='gray')
    # plt.xlim(0,img.shape[1])
    # plt.ylim(0, img.shape[0])
    plt.show()

    x_dif = x_dif[1:-1]
    y_dif = y_dif[1:-1]
if __name__ == "__main__":
    aufgabe1()