import pyrealsense2.pyrealsense2 as rs
import numpy as np

class RealSense:
    def __init__(self):
        width = 1280
        height = 720
        self.pipeline = rs.pipeline()
        config = rs.config()
        config.enable_stream(rs.stream.depth, width, height, rs.format.z16, 30)
        config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, 30)
        self.pipeline.start(config)

    def grab_frame(self):
        frame = self.pipeline.wait_for_frames()
        depth_frame = frame.get_depth_frame()
        color_frame = frame.get_color_frame()
        
        depth_frame = np.asanyarray(depth_frame.get_data())
        color_frame = np.asanyarray(color_frame.get_data())
        if depth_frame is None or color_frame is None:
        #if not depth_frame or not color_frame:
            print("No frames detected, check camera connection")
            exit(1)
        return True, depth_frame, color_frame
    
    def release_frame(self):
        self.pipeline.stop()
