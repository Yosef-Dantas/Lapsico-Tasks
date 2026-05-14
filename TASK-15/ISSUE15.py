import cv2

cam = cv2.VideoCapture(0)

while True:
    sucesso, frame = cam.read()
    frame_redimensionado = cv2.resize(frame, (920,720))
    frame_cinza = cv2.cvtColor(frame_redimensionado, cv2.COLOR_BGR2GRAY)
    # aplicando filtro de canny com a imagem redimensionada e cinza utilizando os valores de teste para "brincar" com as bordas.
    frame_alto = cv2.Canny(frame_cinza, 50, 100)
    cv2.imshow("Imagem em canny: ", frame_alto)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
       

