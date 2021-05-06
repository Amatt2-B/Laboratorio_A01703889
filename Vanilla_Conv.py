#se importan las librerias
import numpy as np
import cv2
import matplotlib.pyplot as plt


def convolucion (img, kernel):
    #Convierte ambas entradas a matrices con ayuda de numpy
    mat = np.matrix(img)
    kernel = np.matrix(kernel)
    #Obtiene las dimensiones de la matriz resultante
    row = (np.shape(mat)[0] - (np.shape(kernel)[0]/2) * 2) + 1
    col = (np.shape(mat)[1] - (np.shape(kernel)[1]/2) * 2) + 1
    
    #Crea la matriz resultante, con valores de cero
    final = np.zeros((int(row), int(col)), dtype = int)
