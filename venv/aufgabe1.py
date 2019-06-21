import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def aufgabe1():
    # ausgelegt auf bilder mit gleicher höhe wie breite
    # lädt bild in graustufen
    image = Image.open("../resources/pic2.jpg").convert("L")
    img = np.asarray(image).astype(dtype='int64')

    # berechne hier die ableitungen, indem man zeilenweise
    h = 1
    x_dif = np.zeros(img.shape).astype(dtype='int64')
    y_dif = np.zeros(img.shape).astype(dtype='int64')

    # berechne hier die ableitung für x, indem man zeilenweise die ableitung
    # von 2h-weit entfernten punkten berechnet
    for y in range(img.shape[0]):
        for x in range(1, img.shape[1] - h):
            x_dif[y][x] = (img[y][x + h] - img[y][x - h]) / 2 * h

    # berechne hier die ableitung für y, indem man spaltenweise die ableitung
    # von 2h-weit entfernten punkten berechnet
    for x in range(img.shape[1]):
        for y in range(1, img.shape[0] - h):
            y_dif[y][x] = (img[y - h][x] - img[y + h][x]) / 2 * h

    deriv = np.zeros((y_dif.shape[0], x_dif.shape[1]))
    for x in range(1, x_dif.shape[1] - h):
        for y in range(1, y_dif.shape[0] - 1):
            deriv[y][x] = np.sqrt(x_dif[y][x] ** 2 + y_dif[y][x] ** 2)

    # plotte bild

    plt.subplot(221)
    plt.imshow(img, cmap='gray')
    plt.subplot(222)
    plt.imshow(x_dif, cmap='gray')
    plt.subplot(223)
    plt.imshow(y_dif, cmap='gray')
    plt.subplot(224)
    plt.imshow(deriv, cmap='gray')

    plt.show()


if __name__ == "__main__":
    aufgabe1()
