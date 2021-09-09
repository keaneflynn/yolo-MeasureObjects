import json
from datetime import datetime

class FileOutput:
    def __init__(self, samplename, main_dataVector):
        self.date = str(datetime.now())
        self.samplename = samplename 
        self.classname = main_dataVector[0] 
        self.confidence = main_dataVector[1] 
        self.length = main_dataVector[2] 
        self.height = main_dataVector[3]

        vector_inputs = [self.date,
                         self.samplename,
                         self.classname,
                         self.confidence,
                         self.length,
                         self.height]

    def test_json(self):
        test = print(vector_inputs)

        return test

    def to_json(self):
        indexList_length = len(self.classname)
        for i in range(indexList_length):
            json_out = {
            "date": self.date,
            "sample_name": self.samplename,
            "class_name": self.classname[i],
            "confidence": self.confidence[i],
            "length_mm": self.length[i],
            "height_mm": self.height[i],
            }

            return json.dumps(json_out, indent=4)
