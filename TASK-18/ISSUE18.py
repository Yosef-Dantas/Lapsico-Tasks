import cv2
from matplotlib import pyplot

imagem = cv2.imread(r"C:\Users\yosef\Desktop\Lapiscos -Tasks\Lapsico-Tasks\TASK-18\arara.jpg")
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
# calculando laplaciano(CV_64F protege as bordas negativas de serem apagadas)
lap = cv2.Laplacian(imagem_cinza, cv2.CV_64F)
# normalizando essa variável(Matriz de entrada, destination, lmt_inf, limt_sup, função para converter números e função para voltar para os 8 bits)
lap = cv2.normalize(lap, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

h_lap = cv2.calcHist([lap], [0], None, [256],[0, 256])

pyplot.figure(figsize=(8, 5))

pyplot.subplot(1, 2, 1)
pyplot.title("Bordas detectadas")
pyplot.imshow(lap, cmap='gray')

pyplot.subplot(1, 2, 2)
pyplot.plot(h_lap)

pyplot.tight_layout()
pyplot.show()
