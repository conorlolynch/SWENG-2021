
"""
Early Steps (Non anaconda approach)
1) Make sure Python 3.5+ is installed
2) Make sure you pip install opencv-python (4.3.0.36 is the version I am using)
3) Test that the pip install works for opencv (test importing it)

Early Steps (Anaconda approach)
1) Create Anaconda Virtual Environment: conda create --name opencv-env python=3.8
2) Activate the environment: conda activate opencv-env
3) Enter the command: pip freeze to see what python modules are installed
4) Deactivate the environment by: conda deactivate

Design Steps
-------------------------------------------------------------------------------
1) Now need to think about how we get the video into the python program
2) What kind of processing do we need to do with the video
3) What do we do with the data generated?

"""

import cv2

# Here is the main function
def main():
    print("Hello")

main()
