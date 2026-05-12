import cv2
import numpy
# Foi feito a importação da imagem, mudança de cor e mostrando na interface.
imagem = cv2.imread("C:\\Users\\LABIC\\Desktop\\Yosef Lab\\LAPISCO-TASKS-1\\TASK-10\\paisagem.jpg")
imagem_cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
cv2.imshow("Paisagem cinza:", imagem_cinza)
# Transformando a imagem em matriz.
linhas, colunas = imagem_cinza.shape
nova_matriz = numpy.zeros((linhas,colunas))
# Dando valor como média para conseguir fazer a varredura manual
limiar= 127
# Fazendo a varredura manual para a limiarização.
for i in range(linhas):
    for j in range(colunas):
        if imagem_cinza[i][j] > limiar:
            nova_matriz[i][j] = 255
        else:
            nova_matriz[i][j] = 0
#Salvando a mtriz como arquivo. 
with open("Matriz_Paisagem.txt", "w")as matriz_paisagem:
    for i in range(linhas):
        matriz_paisagem.write(str(nova_matriz[i]) + "\n")
# Mostrando na interface e salvando a imagem cinza e limiarizada.
cv2.imshow("Paisagem Cinza Limirizada: ", nova_matriz.astype(numpy.uint8))
cv2.imwrite("Paisagem_Cinza_Limirizada.jpg", nova_matriz)
cv2.waitKey(0)
cv2.destroyAllWindows()
