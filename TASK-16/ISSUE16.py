import cv2
from matplotlib import pyplot
# importa-se essa biblioteca para visualizar o histograma como um gráfico. 

imagem = cv2.imread(r"C:\Users\yosef\Desktop\Lapiscos -Tasks\Lapsico-Tasks\TASK-16\arara.jpg")
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# usar função para equalização
imagem_equalizada = cv2.equalizeHist(imagem_cinza)
# calculando o histogramas, o 1 0 é o canal, o none mostra sem máscara, o 256 é qunatas barras tem, e os dois juntos é intervalo dos valores.
h_original = cv2.calcHist(imagem_cinza, [0], None, [256], [0, 256])
h_equalizada = cv2.calcHist(imagem_equalizada, [0], None, [256], [0, 256])

cv2.imshow("Original: ", imagem_cinza)
cv2.imshow("Equalizada: ", imagem_equalizada)

# Para mostrar os histrogramas, funções do matplotlib.
# figure serve para criar uma janela para montar as coisas e o figsize é para definir o tamanho decidido pela pessoa.
pyplot.figure(figsize=(5, 5))

# Pega a janela criada e divide em uma tabela, os valores dentro, controla como o desenho na tabela vai ser feito.
pyplot.subplot(1, 2, 1)
pyplot.title("Histograma Original")
# Cria o histogrma utilizando a variável.
pyplot.plot(h_original)

pyplot.subplot(1, 2, 2)
pyplot.title("Histograma Equalizado")
pyplot.plot(h_equalizada)

pyplot.show()
cv2.waitKey(0)