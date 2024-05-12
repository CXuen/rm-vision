import cv2 
import numpy as np
import detect
from RG import detect_colored

image_path = '/home/xuen/桌面/week-9/pt/a.png'
#'/home/xuen/桌面/week-9/pt/b.jpeg','/home/xuen/桌面/week-9/pt/c.jpeg','/home/xuen/桌面/week-9/pt/d.png','/home/xuen/桌面/week-9/pt/e.jpeg
image = cv2.imread(image_path)

# 红绿点图像
RedGreen_image = detect_colored(image_path)

# 角点和中点坐标图像
corner_image = detect.detect_rectangles(image_path)

# 图像叠加
Final_image = cv2.addWeighted(corner_image, 0.5, RedGreen_image, 0.5, 0)

# 保存路径
Upload_Str1 = r'week-9/save/a_output.jpeg'

# 保存图像
cv2.imwrite(Upload_Str1, Final_image)

# 显示结果
cv2.imshow('Final Image',Final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()