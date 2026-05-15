import cv2
import numpy
from matplotlib import pyplot

imagem = cv2.imread(r"C:\Users\yosef\Desktop\Lapiscos -Tasks\Lapsico-Tasks\TASK-17\arara.jpg")
# Separamos em canais, blue, green e red.
b = imagem[:, :, 0]
g = imagem[:, :, 1]
r = imagem[:, :, 2]
# Transformando para cor cinza e garantindo que o resultado seja inteiro.
imagem_cinza = (0.114 * b + 0.587 * g + 0.299 * r).astype(numpy.uint8)

# Calculando o histograma a mão.
hist_original = numpy.zeros(256, dtype=int)
# Tranformando em linha única pelo flatten, deixando o loop mias rápido.
for pixel in imagem_cinza.flatten():
    hist_original[pixel] += 1

# Soma acumulada
S = numpy.zeros(256, dtype=int)
S[0] = hist_original[0]

# Preenchendo a soma acumulada.
for i in range(1, 256):
    S[i] = S[i - 1] + hist_original[i]

# Encontra o primeiro valor não nulo e o total de pixels
S_min = S[S > 0].min()
total_pixels = imagem_cinza.size

# Cria a tabela do mapeamento
S_normalizada = numpy.zeros(256, dtype=numpy.uint8)
for i in range(256):
    # Usando a fórmula padrão de equalização.
    S_normalizada[i] = numpy.round(((S[i] - S_min) / (total_pixels - S_min)) * 255)

# Aplicando os novos pixels na imagem equalizada
imagem_equalizada = S_normalizada[imagem_cinza]

# Calculando o novo histograma para visualização
hist_eq = numpy.zeros(256, dtype=int)
for pixel in imagem_equalizada.flatten():
    hist_eq[pixel] += 1

pyplot.figure(figsize=(9, 6))

pyplot.subplot(2, 2, 1)
pyplot.title("Imagem Cinza (Calculada)")

# usar cmap = 'gray' para dizer ao maplotlib que é para desenhar a imagem em tom cinza.
pyplot.imshow(imagem_cinza, cmap='gray')

pyplot.subplot(2, 2, 2)
pyplot.title("Histograma Original")
# Desenhando os gráficos.
pyplot.plot(hist_original)

pyplot.subplot(2, 2, 3)
pyplot.title("Imagem Equalizada")
# Para desenhar a imagem
pyplot.imshow(imagem_equalizada, cmap='gray')

pyplot.subplot(2, 2, 4)
pyplot.title("Histograma Equalizado")
pyplot.plot(hist_eq)
# Organização para não se chocar
pyplot.tight_layout()
# Entrega a tela pronta.
pyplot.show()