import cv2
from argparse import ArgumentParser
from yolo_detect import *
from realsense import *

def main():
    parser = argparse.ArgumentParser(description='measure detected objects using YOLO')
    parser.add_argument('samplename', type=str, help='unique name or identifier for the sample of data you are collecting')
    args = parser.parse_args()

    while True:

        rs = RealSense()
        yd = YoloDetections()

        input('press enter to begin capture loop . . .')

        _, depth_frame, color_frame = rs.grab_frame() #had 'ret' before underscore
        yd.detection(color_frame)
        yd.object_distance(depth_frame)
        yd.object_length()
        yd.object_height()
        yd.draw_output(color_frame)

        #fo = FileOutput(args.samplename,
        #                self.object_class,
        #                self.object_confidence,
        #                self.object_length_mm,
        #                self.object_height_mm)
        #fo.test_json()

        cv2.imshow("color frame", color_frame)
        
        cv2.waitKey(1)
        
    rs.release_frame()
    cv2.destroyAllWindows()
    exit(1)

if __name__ == '__main__':
    main()
