import cv2

imagem = cv2.imread("Imagens/lena_color_512.tif")

imgGray = cv2.cvtColor(imagem, "COLOR_BGR2GRAY")


cv2.imshow("Lena", imgGray)

cv2.waitKey(10000)
cv2.destroyAlllWindows()
