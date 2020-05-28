import pickle as pkl
import pprint

import numpy


import os
import getopt,sys

# if os.path.exist('./tracks_frame_119.pkl'):
#     print("123")

# with open("config/cameraConfig.json", "w") as f:
with open('tracks_frame_119.pkl', 'rb') as f:
    data = pkl.load(f)
    # print(data)
    pprint.pprint(data)