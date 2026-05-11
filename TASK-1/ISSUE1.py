import cv2
#Imagem foi aberta
imagem = cv2.imread("C:\\Users\\LABIC\\Desktop\\Yosef Lab\\LAPISCO-TASKS-1\\TASK-1\\arara.jpg")
#Imagem foi mostrada pelo computador.
cv2.imshow("Arara: ", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()