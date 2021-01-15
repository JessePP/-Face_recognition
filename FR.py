import cv2 as cv

img = cv.imread('E:\projekty\cascade\zdjecie.jpg', 1)
cv.imshow('Preson', img)
cv.waitKey(0)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('greyp', gray)
haar_cascade = cv.CascadeClassifier('hear.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
print(f'Number of faces found = {len(faces_rect)}')
for(x,y,w,h) in faces_rect :
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=1)
cv.imshow('wykryte', img )

cv.waitKey(0)
