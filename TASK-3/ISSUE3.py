import cv2
# Imagem foi mostrada.
imagem = cv2.imread("C:\\Users\\LABIC\\Desktop\\Yosef Lab\\LAPISCO-TASKS-1\\TASK-3\\arara.jpg")
# Imagem foi dividida em três canais.
azul, verde, vermelho = cv2.split(imagem)
#Os canais foram mostrados e salvos pelo computador.
cv2.imshow("Canal vermelha: ", vermelho)
cv2.imshow("Canal Azul: ", azul)
cv2.imshow("Canal verde: ", verde)
cv2.imwrite("Canal vermelho.jpg", vermelho)
cv2.imwrite("Canal azul.jpg", azul)
cv2.imwrite("Canal verde.jpg", verde)
# Os canais foram unidos, mostrados e salvos pelo computador.
imagem_original = cv2.merge([azul, verde, vermelho])
cv2.imshow("Imagem original: ", imagem_original)
cv2.imwrite("Imagem original.jpg", imagem_original)
cv2.waitKey(0)
cv2.destroyAllWindows()