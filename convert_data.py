# -*- coding: utf-8 -*-
"""convert-data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F6DQCDLjGHO8DrQ7yorNXE5EIHwlkajy
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install pydicom

hgg=os.listdir('/content/drive/MyDrive/datasetBRMN/hgg')
lgg=os.listdir('/content/drive/MyDrive/datasetBRMN/lgg')
print(lgg)

# Convert to JPEG2K via Pillow
# https://github.com/python-pillow/Pillow
 
import os
import pydicom
import glob
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np
from google.colab.patches import cv2_imshow
hgg=os.listdir('/content/drive/MyDrive/datasetBRMN/hgg')
dir='/content/drive/MyDrive/datasetBRMN/hgg/'
newDir = '/content/drive/MyDrive/datasetBRMNpng/hg/'
for f in hgg:  
    ds = pydicom.read_file(dir + f) # read dicom image
    img = ds.pixel_array # get image array
    img_mem = Image.fromarray(img) # Creates an image memory from an object exporting the array interface
    #plt.imshow(img_mem)
    plt.savefig(f"{newDir}{f.replace('.dcm','.png')}" )
#   There is an exception in Kaggle kernel about "encoder jpeg2k not available", please test following code on your local workstation
#   img_mem.save(outdir + f.replace('.dcm','.jp2'))

dir='/content/drive/MyDrive/datasetBRMN/lgg/'
newDir = '/content/drive/MyDrive/datasetBRMNpng/lg/'
for f in lgg:  
    print(f)
    ds = pydicom.read_file(dir + f) # read dicom image
    img = ds.pixel_array # get image array
    img_mem = Image.fromarray(img) # Creates an image memory from an object exporting the array interface
    #plt.savefig(f"{newDir}{f.replace('.dcm','.png')}" )
    plt.imshow(img)
    plt.savefig(f"{newDir}{f.replace('.dcm','.png')}" )
    #plt.show()