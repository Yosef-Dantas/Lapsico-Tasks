import cv2
imagem = cv2.imread("C:\\Users\\LABIC\\Desktop\\Yosef Lab\\LAPISCO-TASKS-1\\TASK-7\\arara.jpg")
imagem_cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
#repeti o que fiz nas questões passsadas, o novo desafio começa à partir daqui.
#apliquei a limiarização, utilizei  o otsu para não calcular a nota de corte menor e utilizei "_," para não aparecer o resultado, testei alguns valores da nota de corte para apresentar resultados diferentes, mostrei a imagem e salvei a imagem. 
_, imagem_1 = cv2.threshold(imagem_cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("imagem_Limirizada", imagem_1)
cv2.imwrite("Imagem.jpg", imagem_1)
cv2.waitKey(0)
cv2.destroyAllWindows