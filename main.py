import os
import fnmatch
from pathlib import Path


os.chdir("\.\Users\Oyola\Desktop")

def ssDetectFile():
    for file in os.listdir("."):
        my_file = Path("./SS")
        if my_file.is_file():
            # file exists
            print "Already Exist..."
        else:
            os.mkdir("SS")

def detection():
    for file in os.listdir("."):
        if fnmatch.fnmatch(file, "Screen Shot" + "*" + ".png"):
            print "Detected"

while True:
    ssDetectFile()
    detection()
