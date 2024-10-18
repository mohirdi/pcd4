import imageio.v3 as i
import numpy as np
import matplotlib.pyplot as plt

im=i.imread("C:\\Users\\rega aditya\\Documents\\regapcd4\\a.jpg")
def eq(im):
    hist,bins = np.histogram(im.flatten(),bins=256,range=[0,256])
    cdf =hist.cumsum()
    cdm = (cdf/cdf.max())*255
    imq = np.interp(im.flatten(),bins[:-1],cdm)
    return imq.reshape(im.shape).astype(np.uint8)

hist,bins =np.histogram(im.flatten(),bins=256,range=[0,256])
imq=eq(im)
hist_e,bins =np.histogram(imq.flatten(),bins=256,range=[0,256])

plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.imshow(im)
plt.subplot(2,2,2)
plt.plot(hist)
plt.subplot(2,2,3)
plt.imshow(imq)
plt.subplot(2,2,4)
plt.plot(hist_e)

plt.show()