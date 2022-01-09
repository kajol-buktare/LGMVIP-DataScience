#library needed to convert image to pencil sketch
import cv2  

#To read the image it's address is given
image = cv2.imread("C:\\Users\\kajol\\OneDrive\\Pictures\\dog.jpg")
cv2.imshow("Dog", image)
cv2.waitKey(0)

#Converting original image to greyscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Dog", gray_image)
cv2.waitKey(0)

#Invert the grayscale image
inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()

#Prcocess blur image by Gaussian function
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

#To invert blurred image
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)

#Shows original image and it's pencil sketch
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)
cv2.imwrite
