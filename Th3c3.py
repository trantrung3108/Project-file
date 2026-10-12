import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r"C:\ThịGiac\Ảnh chụp màn hình 2026-09-24 102716.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sx = cv2.Sobel(gray,cv2.CV_64F,1,0)          
sy = cv2.Sobel(gray,cv2.CV_64F,0,1)         
sobel = cv2.convertScaleAbs(sx) + cv2.convertScaleAbs(sy)
canny = cv2.Canny(gray,100,200)
lap = cv2.convertScaleAbs(cv2.Laplacian(gray,cv2.CV_64F))
plt.subplot(2,2,1); plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)); plt.title('Anh goc')
plt.subplot(2,2,2); plt.imshow(sobel,cmap='gray'); plt.title('Sobel')
plt.subplot(2,2,3); plt.imshow(canny,cmap='gray'); plt.title('Canny')
plt.subplot(2,2,4); plt.imshow(lap,cmap='gray'); plt.title('Laplace')
plt.show()