import cv2
from matplotlib import pyplot

imagem = cv2.imread(r"C:\Users\yosef\Desktop\Lapiscos -Tasks\Lapsico-Tasks\TASK-19\arara.jpg")
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(imagem_cinza,cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(imagem_cinza, cv2.CV_64F, 0, 1, ksize=3 )

m = cv2.magnitude( sobel_x, sobel_y)

m_norm = cv2.normalize(m, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

h_c = cv2.calcHist([imagem_cinza],[0], None, [256], [0, 256])
h_n = cv2.calcHist([m_norm], [0], None, [256], [0, 256])

pyplot.figure(figsize=(8, 5))

pyplot.subplot(2, 2, 1)
pyplot.title("Imagem cinza: ")
pyplot.imshow(imagem_cinza, cmap='gray')
pyplot.subplot(2, 2, 2)
pyplot.plot(h_c)

pyplot.subplot(2, 2, 3)
pyplot.title("Imagem Normalizada: ")
pyplot.imshow(m_norm, cmap='gray')
pyplot.subplot(2, 2, 4)
pyplot.plot(h_n)

pyplot.tight_layout()
pyplot.savefig(r"C:\Users\yosef\Desktop\Lapiscos -Tasks\Lapsico-Tasks\TASK-19\painel_completo.png", dpi=300)
pyplot.show()

