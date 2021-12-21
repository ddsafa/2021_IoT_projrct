import cv2

img = cv2.imread('people.jpg')
cv2.resize (img, (300,100))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('people',img)

while True :
     if cv2.waitKey() == ord('q'):
         break
cv2.imwrite('people.jpg', gray)

cv2.destroyAllWindows()