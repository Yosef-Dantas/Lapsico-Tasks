import cv2
import numpy
# Variáveis
soma_x = 0
soma_y = 0
cpp = 0

Quadrado = cv2.imread("C:\\Users\\LABIC\\Desktop\\Yosef Lab\\LAPISCO-TASKS-1\\TASK-11\\Quadrado.png")
Quadrado_cinza = cv2.cvtColor(Quadrado,cv2.COLOR_BGR2GRAY)
cv2.imshow("Quadrado Cinza: ", Quadrado_cinza)

linhas, colunas = Quadrado_cinza.shape
nova_matriz = numpy.zeros((linhas, colunas), dtype=numpy.uint8)

for i in range(linhas):
    for j in range(colunas):
       nova_matriz[i][j] = Quadrado_cinza[i][j]
    # Verificando se o pixel é preto, como foi feito pelo paint foi usado um número teste já que não há garantia que o pixel é 0.
       if nova_matriz[i][j] < 25:
        soma_y += i
        soma_x += j
        cpp += 1
        
# Cálculo do XC e do YC e do centróide e sua marcação na imagem.
if cpp > 0:
   xc = int(soma_x / cpp)
   yc = int(soma_y/cpp)
   print(f"Centróide em: XC={xc} e YC={yc}")
   
   cv2.circle(Quadrado_cinza, (xc,yc), radius=3, color=255, thickness=1)
   cv2.imshow("Centróide Na Imagem", Quadrado_cinza)
else:
   print("Nenhuma imagem encontrada.")
cv2.waitKey(0)
cv2.destroyAllWindows()