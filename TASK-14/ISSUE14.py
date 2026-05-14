import cv2
# Ativando o canal de comunicação com a webcam.
cam = cv2.VideoCapture(0)

# Loop que garante a repetição infinita
while True:
    # Dando sinal que deu certo e tirando as fotos.
    sucesso, frame = cam.read()
    # Mudando o tamanho do frame como vai aparecer na interface.
    frame_redimensionado = cv2.resize(frame, (920,720))
    # Fazendo a mudança de cor e mostrando na interface.
    frame_cinza = cv2.cvtColor(frame_redimensionado, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame cinza: ", frame_cinza)
    # utilizando essa relação para quando o usuário aperta a letra q para o loop. O número dentro do waitkey muda a velocidade e a fluidez do vídeo.
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


