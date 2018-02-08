import cv2
from glob import glob

images=glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    resized_img=cv2.resize(img,(100,100))
    cv2.imwrite("Resized"+image, resized_img)
