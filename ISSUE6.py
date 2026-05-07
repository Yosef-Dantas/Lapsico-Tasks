import cv2
imagem = cv2.imread("C:\\Users\\LABIC\\Desktop\\Yosef Lab\\LAPISCO-TASKS-1\\TASK-6\\arara.jpg")
imagem_cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem Cinza: ", imagem_cinza)
imagem_alta = cv2.Canny(imagem_cinza, 30, 200)
cv2.imshow("Imagem Alta: ", imagem_alta)
cv2.imwrite("Imagemalta.jpg", imagem_alta)
cv2.waitKey(0)
cv2.destroyAllWindows()