from PIL import Image
import math
img1 = Image.open(r'C:/Users/crab/Desktop/1.jpg')#图片1
img2 = Image.open(r'C:/Users/crab/Desktop/2.jpg')#图片2

#该函数的作用是由于 Image.blend()函数只能对像素大小一样的图片进行重叠，故需要对图片进行剪切。

#进行图片重叠  最后一个参数是图片的权值
final_img2 = Image.blend(img1, img2, (math.sqrt(5)-1)/2)
#别问我为什么是  (math.sqrt(5)-1)/2   这个是黄金比例，哈哈！！
final_img2.show()