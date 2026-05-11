import cv2
# Imagem foi aberta.
imagem = cv2.imread("C:\\Users\\LABIC\\Desktop\\Yosef Lab\\LAPISCO-TASKS-1\\TASK-2\\arara.jpg")
# Imagem foi mostrada.
cv2.imshow("Arara: ", imagem)
# Imagem foi convertida para cor cinza.
imagem_cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
# Nova imagem foi mostrada e salva pelo computador.
cv2.imshow("Arara cinza:", imagem_cinza)
cv2.imwrite("Arara Cinza.jpg", imagem_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()