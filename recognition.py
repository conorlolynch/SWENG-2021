
"""
Early Steps (Non anaconda approach)
1) Make sure Python 3.5+ is installed
2) Make sure you pip install opencv-python (4.3.0.36 is the version I am using)
3) Test that the pip install works for opencv (test importing it)

Design Steps
-------------------------------------------------------------------------------
1) Now need to think about how we get the video into the python program
2) What kind of processing do we need to do with the video
3) What do we do with the data generated?

"""

import cv2, sys

# Get user supplied values
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)


# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)


# Here is the main function
def main():
    print("Testing")

main()
