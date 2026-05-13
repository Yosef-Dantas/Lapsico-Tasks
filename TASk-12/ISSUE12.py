import cv2
import numpy

Matriz = r"C:\Users\LABIC\Desktop\Yosef Lab\LAPISCO-TASKS-1\TASk-12\Matriz_Paisagem.txt"

with open(Matriz, "r") as arquivo:
    # Tirando a quebra de linha falsa e substituindo por espaço.
    texto = arquivo.read().replace('n', ' ')
    # Utiliza ] para falar onde a linha termina e tira todas as [.
    Matriz_limpa = (linha.replace('[', ' ') for linha in texto.split(']') if linha.strip())
    # Lê dados e transforma. 
    dtxt = numpy.genfromtxt(Matriz_limpa)

# Transforma os dados em imagem, exibe e salva.
imagem_cinza = numpy.array(dtxt, dtype=numpy.uint8)
cv2.imshow("Imagem Cinza: ", imagem_cinza)
cv2.imwrite("Imagem.jpg", imagem_cinza)

cv2.waitKey(0)
cv2.destroyAllWindows()