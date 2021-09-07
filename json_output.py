import json
from datetime import datetime

class fileOutput:
    def __init__(self, self.object_class, self.object_class, self.object_confidence, self.object_length_mm, self.object_height_mm):
        self.date = str(datetime.now())
        self.samplename = # include with argparse
        self.classname = self.object_class # output from neural network
        self.scores = self.object_confidence # confidence from neural network
        self.length = self.object_length_mm # length of measured object (mm)
        self.height = self.object_height_mm # height of measured object (mm)

    def to_json(self):
        json_out = {
            "date": self.date,
            "sample_name": self.samplename,
            "class_name": self.classname,
            "confidence": self.scores,
            "length_mm": self.length,
            "height_mm": self.height,
            }

        return json.dumps(json_out)
