import cv2
import numpy as np
import os
# from os.path import isfile, join

root_path = '/home/msdc/jcgarciaca/projects/drone/process_video'
frames_folder = os.path.join(root_path, 'frames', 'GX016807')
num_frames = len(os.listdir(frames_folder))
dst_video = os.path.join(root_path, 'videos', 'GX016807_slow_2.mp4')

frame_array = []
fps = 1

# for num in range(num_frames):
for num in range(200, 3000):
	print('Processing frame {}'.format(num))
	if num % fps == 0:
		filename = os.path.join(frames_folder, 'img_' + str(num) + '.jpg')
		img = cv2.imread(filename)
		
		img = cv2.resize(img, (1280, 720), interpolation = cv2.INTER_AREA)
		
		height, width, layers = img.shape
		size = (width,height)
		frame_array.append(img)


out = cv2.VideoWriter(dst_video,cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

for frame in frame_array:
	out.write(frame)
out.release()
