import json
from datetime import datetime
import os
import numpy as np

class FileOutput:
    def __init__(self, samplename, main_dataVector):
        self.date = str(datetime.now())
        self.filedate = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
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
            filename = self.samplename+'_'+str(self.filedate)+'_'+str(i+1)
            json_out = {
            "date": self.date,
            "sample_name": self.samplename,
            "class_name": class_list[self.classname[i]],
            "confidence": np.float64(self.confidence[i]),
            "length_mm": np.float64(self.length[i]),
            "height_mm": np.float64(self.height[i]),
            }
            
            with open("{}/{}.json".format(directory, filename), 'w') as f:
                json.dump(json_out, f)
