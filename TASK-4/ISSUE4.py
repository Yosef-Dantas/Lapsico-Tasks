import cv2
imagem = cv2.imread("C:\\Users\\LABIC\\Desktop\\Yosef Lab\\LAPISCO-TASKS-1\\TASK-4\\arara.jpg")
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
cv2.imshow("Tons: ", h)
cv2.imshow("Saturação:", s)
cv2.imshow("Brilho: ", v)
cv2.imwrite("Tons.jpg", h)
cv2.imwrite("Saturação.jpg", s)
cv2.imwrite("Brilho.jpg", v)
cv2.waitKey(0)
cv2.destroyAllWindows