import cv2
import os
import sys

root_path = sys.argv[1]
videos_folder = os.path.join(root_path, 'videos')
target_folder = os.path.join(root_path, 'frames')

video_lst = os.listdir(videos_folder)
subfolder = False
for video_name in video_lst:
	video_path = os.path.join(videos_folder, video_name)

	if subfolder and not os.path.exists(os.path.join(target_folder, video_name)):
		os.makedirs(os.path.join(target_folder, video_name))

	cap = cv2.VideoCapture(video_path)
	length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	fps = round(cap.get(cv2.CAP_PROP_FPS))
	interval = fps / 5
	print(video_name + ' - length: ' + str(length) + ' - FPS: ' + str(fps))
	
	if (cap.isOpened()== False):
		print("Error opening video stream or file")

	counter = 1
	while(cap.isOpened()):
		ret, frame = cap.read()	
		if ret == True:
			print('Processing frame {}/{}'.format(counter + 1, length))
			if counter%interval == 0:
				print('Saving frame')
				if subfolder:
					cv2.imwrite(os.path.join(target_folder, video_name, 'img_' + str(counter) + '.jpg'), frame)
				else:
					cv2.imwrite(os.path.join(target_folder, video_name.split('.')[0] + '_img_' + str(counter) + '.jpg'), frame)
			counter += 1
		if counter > length:
			break