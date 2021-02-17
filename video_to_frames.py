import cv2
import os
import sys

root_path = sys.argv[1]
videos_folder = os.path.join(root_path, 'videos')
target_folder = os.path.join(root_path, 'frames')

video_name = 'DJI_0289_alto'
video_path = os.path.join(videos_folder, video_name + '.MP4')

if not os.path.exists(os.path.join(target_folder, video_name)):
	os.makedirs(os.path.join(target_folder, video_name))

cap = cv2.VideoCapture(video_path)
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('length:', length)

if (cap.isOpened()== False):
	print("Error opening video stream or file")
counter = 1
while(cap.isOpened()):
	ret, frame = cap.read()	
	if ret == True:
		print('Processing frame {}/{}'.format(counter + 1, length))
		cv2.imwrite(os.path.join(target_folder, video_name, 'img_' + str(counter) + '.jpg'), frame)
		counter += 1
	if counter > length:
		break	