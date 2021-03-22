import os
import time
index = 52
image_ext = ['.jpg', '.jpeg']



while(True):
	image_files = [f for f in os.listdir('.') if os.path.splitext(f)[1].lower() in image_ext]
	for i in image_files:
		if (not "naruto" in os.path.splitext(i)[0]):
			index = index+1
			os.rename(i,"naruto_" + str(index) + ".jpg")
	time.sleep(10)