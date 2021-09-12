import json
from datetime import datetime
import os

class FileOutput:
    def __init__(self, samplename, main_dataVector):
        self.date = str(datetime.now())
        self.samplename = samplename 
        self.classname = [i[0] for i in main_dataVector[0]]
        self.confidence = [i[0] for i in main_dataVector[1]] 
        self.length = main_dataVector[2] 
        self.height = main_dataVector[3]

        self.vector_inputs = (self.date,
                              self.samplename,
                              self.classname,
                              self.confidence,
                              self.length,
                              self.height)

    def test_json(self, class_list):
        indexList_length = len(self.classname)
        for i in range(indexList_length):
            self.vector_inputs = (self.date,
                                  self.samplename,
                                  class_list[self.classname[i]],
                                  self.confidence[i],
                                  self.length[i],
                                  self.height[i])
            print(self.vector_inputs)
        return self.vector_inputs

    def to_json(self, class_list):
        indexList_length = len(self.classname)
        directory = 'outfile'
        for i in range(indexList_length):
            filename = self.samplename+'_'+str(i)
            json_out = {
            "date": self.date,
            "sample_name": self.samplename,
            "class_name": class_list[self.classname[i]],
            "confidence": self.confidence[i],
            "length_mm": self.length[i],
            "height_mm": self.height[i],
            }
            
            with open("{}/{}.json".format(directory, filename), 'w') as f:
                json.dump(str(json_out), f)
