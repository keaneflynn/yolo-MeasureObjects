import cv2
from yolo_detect import *
from realsense import *

while True:

    rs = RealSense()
    yd = YoloDetections()

    input('press enter to continue . . .')

    ret, depth_frame, color_frame = rs.grab_frame()
    yd.detection(color_frame)
    yd.object_distance(depth_frame)
    yd.object_length()
    yd.object_height()
    yd.draw_output(color_frame)

    cv2.imshow("color frame", color_frame)
    
    cv2.waitKey(1)
    
rs.release_frame()
cv2.destroyAllWindows()
exit(1)
