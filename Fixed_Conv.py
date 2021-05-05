
import numpy as np
import cv2
import matplotlib.pyplot as plt
 
def conv_help(fragment, kernel):
    
    f_row, f_col = fragment.shape
    k_row, k_col = kernel.shape 
    result = 0.0
    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row,col] *  kernel[row,col]
    return result

def conv(foto, kernel):
    #Aplica una convolucion de una dimesion y da matriz resultante
    
    foto_row, foto_col = foto.shape #se asigna numero de filas y numero de columnas de la foto o matriz
    kernel_row, kernel_col = kernel.shape #asigna num de filas y columnas de filtro o matriz kernel
   
    output = np.zeros(image.shape) #matriz donde guardo el resultado
    #al inicio se guardaran valores de ceros, con largo y ancho determinados
   
    for row in range(foto_row):
        for col in range(foto_col):
                output[row, col] = conv_help(
                                    foto[row:row + kernel_row, 
                                    col:col + kernel_col],kernel)
             
    plt.imshow(output, cmap='gray')
    plt.title("Imagen utilizando matriz de Kernel".format(kernel_row, kernel_col))
    plt.show()
 
    return output #se presenta tercera matriz