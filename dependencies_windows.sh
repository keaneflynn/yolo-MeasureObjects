#!/bin/bash

for var in pyrealsense2 opencv-python argparse DateTime numpy
do
yes | pip install $var
done
