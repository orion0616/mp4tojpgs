import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture('2017_0923_145145_003.MP4')
success,image = vidcap.read()
count = 0
success = True
# count = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
# print(count)
while success:
    for i in range(6):
        success,image = vidcap.read()
    print('Read a new frame: ', success)
    cv2.imwrite("frame_%d.jpg" % count, image)     # save frame as JPEG file
    count += 1
