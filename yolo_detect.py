import cv2

class YoloDetections:
    def __init__(self):
        self.confidence = 0.3
        self.nms = 0.2
        self.colors = [(255, 255, 0), (0, 255, 255), (0, 255, 0), (255, 0, 0)]
        self.sensor_width_mm = 3.68 #3.896
        self.sensor_height_mm = 2.1
        self.focal_length = 1.88
        self.image_width_pixels = 1280
        self.image_height_pixels = 720

        self.class_names = []
        with open("model_data/coco.names.txt", "r") as f:
            self.class_names = [cname.strip() for cname in f.readlines()]
        
        #loading yolo net
        net = cv2.dnn.readNet("model_data/yolov4-tiny.weights","model_data/yolov4-tiny.cfg.txt")
        #net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA) #Use with GPU?
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        #net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16) #Use with GPU?
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        self.model = cv2.dnn_DetectionModel(net)
        self.model.setInputParams(size=(416, 416), scale=1 / 255, swapRB=True)

        self.box_width = []
        self.box_height = []
        self.object_boxes = []
        self.object_centroid = []
        self.object_class = []
        self.object_confidence = []
        self.object_distances = []
        self.object_height_mm = []
        self.object_length_mm = []
        self.depth_centroid = [] #where center x and y are switched in order because that is the format that RealSense accepts

    def detection(self, color_frame):
        self.classes, self.scores, self.boxes = self.model.detect(color_frame, self.confidence, self.nms)
        self.detection_count = len(self.boxes)    
        
        for i in range(self.detection_count):
            #Loop over detections and create an array with all of the important info for each detection
            self.box_width.append(self.boxes[i, 2])
            self.box_height.append(self.boxes[i, 3])
            center_x = ((self.box_width[i] // 2) + self.boxes[i, 0])
            center_y = ((self.box_height[i] // 2) + self.boxes[i, 1])
            self.object_boxes.append(self.boxes[i])
            self.object_centroid.append((center_x, center_y))
            self.depth_centroid.append((center_y, center_x))
            self.object_class.append(self.classes[i])
            self.object_confidence.append(self.scores[i])

        return self.object_boxes, self.object_centroid, self.object_class, self.object_confidence
        
    def object_distance(self, depth_frame):
        for i in range(self.detection_count):
            self.object_distances.append(depth_frame[self.depth_centroid[i]])
        return self.object_distances

    def object_length(self):
        for i in range(self.detection_count):
            self.object_length_mm.append((self.object_distances[i] * self.box_width[i] * self.sensor_width_mm) / (self.focal_length * self.image_width_pixels))
        return self.object_length_mm

    def object_height(self):
        for i in range(self.detection_count):
            self.object_height_mm.append((self.object_distances[i] * self.box_height[i] * self.sensor_height_mm) / (self.focal_length * self.image_height_pixels))
        return self.object_height_mm

    def draw_output(self, color_frame):
        for (classid, score, box, length) in zip(self.object_class, self.object_confidence, self.object_boxes, self.object_length_mm):
            color = self.colors[int(classid) % len(self.colors)]
            frame_label = "%s : %f, %i mm wide" % (self.class_names[classid[0]], score, round(length))
            cv2.rectangle(color_frame, box, color, 2)
            cv2.putText(color_frame, frame_label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        #print(self.object_class)
    def json_data(self):
        class_list = self.class_names
        main_dataVector = (self.object_class,
                           self.object_confidence,
                           self.object_length_mm,
                           self.object_height_mm)
        return(main_dataVector, class_list)
        
