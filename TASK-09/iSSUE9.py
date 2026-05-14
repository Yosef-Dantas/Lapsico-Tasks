import cv2
import numpy

imagem = cv2.imread("C:\\Users\\LABIC\\Desktop\\Yosef Lab\\LAPISCO-TASKS-1\\TASK-9\\paisagem.jpg")
imagem_cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
cv2.imshow("Paisagem Cinza: ", imagem_cinza)

linhas, colunas = imagem_cinza.shape
nova_matriz = numpy.zeros((linhas, colunas))
for i in range(linhas):
    for j in range(colunas):
        nova_matriz[i][j] = imagem_cinza[i][j]

with open("Matriz_arara.txt", "w") as matriz_arara:
    for i in range(linhas):
        matriz_arara.write(str(nova_matriz[i]) + "\n")

cv2.waitKey(0)
cv2.destroyAllWindows()