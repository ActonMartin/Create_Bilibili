import cv2
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont

'''
功能是给音频创建同名称的图片作为后面的视频的画面内容。
'''


class PutText():

	def __init__(self):
		self.path = "E:\\Pandownload\\04 数据结构与算法之美\\mp3"
		self.text_list = []
		for files in os.listdir(self.path):
			name = files.split(".")[0]
			self.text_list.append(name)
		self.create_image()
		self.font = cv2.FONT_HERSHEY_SIMPLEX

	def create_image(self):
		img = np.zeros([1080, 1920, 3], np.uint8)
		img[:, :, 0] = np.zeros([1080, 1920]) + 250
		img[:, :, 1] = np.ones([1080, 1920]) + 235
		img[:, :, 2] = np.ones([1080, 1920]) * 215
		cv2.imwrite("background.jpg", img)
		return img

	def put_text(self):
		img = cv2.imread("background.jpg")
		font = ImageFont.truetype("./simhei.ttf", 50, encoding="utf-8")
		for i in self.text_list:
			cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			pillow_img = Image.fromarray(cv2img)
			draw = ImageDraw.Draw(pillow_img)
			print(i)
			draw.text((10,540), i, (220,20,60), font=font)
			cv2charimg = cv2.cvtColor(np.array(pillow_img), cv2.COLOR_RGB2BGR)
			cv2.imencode('.jpg', cv2charimg)[1].tofile(i +str(".jpg"))

if __name__ == "__main__":
	PutText().put_text()