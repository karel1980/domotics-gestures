#!/usr/bin/env python

import sys
import cv2

def record():
    print("writing output.avi")
    print("press any key to stop recording")

    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    for i in range(300):
        success, buf = cap.read()
        out.write(buf)

    out.release()
    cap.release()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: record.py [filename]")
        print("This will record a video file")
        exit()
    record()
