#!/Users/jaspergilley/venv/bin/python3
import numpy as np
import cv2
import colorMappings
import pdb
from time import sleep

image = cv2.imread("static.png")
cap = cv2.VideoCapture('d3short1.mp4')

def writeFromMask(this_image, colorRange: tuple, outputName="default") -> None:
    lower, upper = colorRange
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    # find the colors within the specified boundary and apply the mask
    mask = cv2.inRange(this_image, lower, upper)
    output = cv2.bitwise_and(this_image, image, mask=mask)

    cv2.imwrite(f"outputs/video/parsed-{outputName}.png", output)

if __name__=="__main__":
    success,image = cap.read()
    count = 0
    while success:
        writeFromMask(image, colorMappings.ranges["cr3"], outputName=f"cr3-2-{count}")
        success,image = cap.read()
        count += 1
        print(count, "of 345")

    """
    for key, value in colorMappings.ranges.items():
        writeFromMask(image, value, outputName=key)
    """