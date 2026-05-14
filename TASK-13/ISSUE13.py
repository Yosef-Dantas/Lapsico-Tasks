import cv2
import numpy
# Utilizando kernel
Sx = numpy.array([
    [-1, 0, 1],   
    [-2, 0, 2],   
    [-1, 0, 1]    
])
Sy = numpy.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

imagem = cv2.imread(r"C:\Users\yosef\Desktop\Lapiscos -Tasks\Lapsico-Tasks\TASK-13\arara.jpg")
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem: ",imagem_cinza)

linhas,  colunas = imagem_cinza.shape
matriz = numpy.zeros((linhas, colunas), dtype=numpy.uint8)

for i in range(1, linhas -1):
    for j in range(1, colunas -1):
        x = (
            (imagem_cinza[i-1][j-1] * Sx[0][0]) + (imagem_cinza[i-1][j] * Sx[0][1]) + (imagem_cinza[i-1][j+1] * Sx[0][2]) +
            (imagem_cinza[i][j-1]   * Sx[1][0]) + (imagem_cinza[i][j]   * Sx[1][1]) + (imagem_cinza[i][j+1]   * Sx[1][2]) +
            (imagem_cinza[i+1][j-1] * Sx[2][0]) + (imagem_cinza[i+1][j] * Sx[2][1]) + (imagem_cinza[i+1][j+1] * Sx[2][2])   
        )

        y = (
            (imagem_cinza[i-1][j-1] * Sy[0][0]) + (imagem_cinza[i-1][j] * Sy[0][1]) + (imagem_cinza[i-1][j+1] * Sy[0][2]) + 
            (imagem_cinza[i][j-1]   * Sy[1][0]) + (imagem_cinza[i][j]   * Sy[1][1]) + (imagem_cinza[i][j+1]   * Sy[1][2]) + 
            (imagem_cinza[i+1][j-1] * Sy[2][0]) + (imagem_cinza[i+1][j] * Sy[2][1]) + (imagem_cinza[i+1][j+1] * Sy[2][2])
        )
        magnitude = abs(x) + abs(y)

        if magnitude > 255:
            magnitude = 255
        matriz[i][j] = magnitude

cv2.imshow("Imagem por sobel:", matriz)
cv2.imwrite("Imagem.jpg", matriz)

cv2.waitKey(0)
cv2.destroyAllWindows()


