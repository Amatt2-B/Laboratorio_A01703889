import numpy as np

m = np.matrix('1 2 3 4 5 6; 7 8 9 10 11 12; 0 0 1 16 17 18; 0 1 0 7 23 24; 1 7 6 5 4 3')
k = np.matrix('1 1 1; 0 0 0; 2 10 3')
row = (np.shape(m)[0] - (np.shape(k)[0]/2) * 2) + 1
col = (np.shape(m)[1] - (np.shape(k)[1]/2) * 2) + 1


vanilla = np.zeros((int(row), int(col)), dtype = int)

num1 = 0
for i in range (np.shape(m)[0] - np.shape(k)[0] + 1):
    for j in range (np.shape(m)[1] - np.shape(k)[1] + 1):
        num1 += np.multiply((m[i:i + (np.shape(k)[0]), j:j + (np.shape(k)[1])]), k)
        vanilla[i][j] = num1.sum()
        num1 = 0
print(vanilla)