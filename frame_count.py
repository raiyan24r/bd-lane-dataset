import cv2
import os




def video_info(filename):
    video = cv2.VideoCapture(filename)

 
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS) 
    # print(fps)clea
    duration =frame_count / fps
    return duration, frame_count

videoDir = r'H:\Thesis 400\1.Dataset_Creation\BD-Dataset Creation'


count=0
total_frames=0
total_duration=0

for subdirs, dirs, files in os.walk(videoDir):
    for file in files:
        print(file)
        count+=1

        vid=video_info(videoDir+'\\' + file)
        total_duration+=vid[0]
        total_frames+=vid[1]
        # print(total_frames)
    #     if count==1 :
    #         break
    # if count==1 :
    #     break

print(total_duration)
print(total_frames)


