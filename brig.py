import imageio.v3 as i
import numpy as np
import matplotlib.pyplot as plt



def bl(image1,op1,image2,op2):
    img1 =image1.astype(np.float32)
    img2 =image2.astype(np.float32)
    imbl=(img1*op1)+(img2*op2)
    imbl = np.clip(imbl,0,255)
    return imbl.astype(np.uint8)


img1=i.imread("C:\\Users\\rega aditya\\Documents\\regapcd4\\1.jpg")
img2=i.imread("C:\\Users\\rega aditya\\Documents\\regapcd4\\2.jpg")
imbl=bl(img1,0.3,img2,0.7)
hist1,bins = np.histogram(img1.flatten(),bins=256,range=[0,256])
hist2,bins = np.histogram(img2.flatten(),bins=256,range=[0,256])
histb,bins = np.histogram(imbl.flatten(),bins=256,range=[0,256])


plt.figure(figsize=(10,10))
plt.subplot(3,2,1)
plt.imshow(img1)
plt.subplot(3,2,2)
plt.plot(hist1)

plt.subplot(3,2,3)
plt.imshow(img2)
plt.subplot(3,2,4)
plt.plot(hist2)

plt.subplot(3,2,5)
plt.imshow(imbl)
plt.subplot(3,2,6)
plt.plot(histb)

plt.show()