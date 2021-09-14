# Yolo Object Detection with Distance Measurement and Bounding Box Dimensions


In this project, we will be using YOLOv4 object detection combined with an Intel Realsense D455i camera to measure the width and height of whatever object we are detecting with the YOLO CNN.

![image](https://github.com/keaneflynn/yolo-MeasureObjects/blob/master/media/cupMeasurement.png)
*The above image shows a blue camp mug detected based on a crudely trained yolov4-tiny neural network that is measuring the width of the mug at 129mm when I have ground truthed the width of the mug, including the handle, to be 128mm*

## Current Use
In its current working state, this program will detect objects from whatever YOLO neural network you choose (should work for Yolov3*, Yolov3-tiny*, Yolov4, and Yolov4-tiny *untested*) and will display the image and place a bounding box around the object, label it, give a confidence score, and show how wide the object is in millimeters (this can easily be swapped over to object height by substituting yd.object_height() for yd.object_length() in the depth_detect.py file). Additionally, it will kick out a .json file for every object detected in the frame, so if there are 4 objects it will return 4 .json files with relevant metrics. The .json files will have the following format: samplename_MM-DD-YYYY-HH-MM-SS_#.json.
Unfortunately I have only been able to test this on Windows operating system as Intel does not support this camera use with Mac OS.

To run the program simply move into the project directory in your terminal (I recommend Powershell), and type out the following:                      
      ``` python depth_detect.py --samplename ```

You will then be prompted to hit enter to capture an image and allow the program to proceed forward. Each subsequent time the user hits enter, it will capture a new image and run the detection and measurement on a new image generated at the time you hit the enter button. To exit the program, simply hit control + c to keyboard interrupt the program. It currently has an issue of hanging up the terminal after it quits but I will fix that as soon as I can.

## Future upgrades
I will likely add support for use with Nvidia Jetson products in the near future as well as a docker container to allow this program to run on Mac OS or whatever the hell you want, go wild.

Shoot me a message for any other cool stuff you think would go well in this program. Cheers.
