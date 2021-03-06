#Importar librerías
import numpy as np
import math
import cv2
import matplotlib.pyplot as plt

#Dimensiones de la matriz de la imagen
#500x1100

def padding (matriz, rows, cols):
    #Convertir la lista de listas a matriz con numpy
    matriz = np.matrix(mat)
    #Cantidad de renglones y columnas más que la matriz original
    m = math.floor((rows - np.shape(matriz)[0]) / 2)
    n = math.floor((cols - np.shape(matriz)[1]) / 2)
    
    #Se genera la matriz final con las dimensiones especificadas
    final = np.zeros((rows, cols))
    
    #Se inicia el ciclo for
    for i in range (np.shape(matriz)[0]):
        for j in range (np.shape(matriz)[1]):
            #Se suma m y n para ignorar ciertos renglones y columnas
            final[i + m][j + n] = mat[i, j]
    #Se imprime la matriz final
    plt.imshow(final, cmap='gray')
    plt.title("Padding de imagen")
    plt.show()
    
#Pedir la matriz original (imagen), y las dimensiones de la matriz solicitada
#Nombre del archivo = foto.jpg
imagen = input('Nombre del archivo ')
img = cv2.imread(imagen, cv2.IMREAD_GRAYSCALE)
rows = int(input('Numero de Filas '))
cols = int(input('Numero de Columnas '))

#Llamar la función padding, mandando la matriz y las dimensiones 
padding(img, rows, cols)