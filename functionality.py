"""
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([])
    upper_blue = np.array([])

    cv2.imshow('frame', hsv)
    
    if cv2.waitKey(1) == ord('z'):
        break



cap.release()
cv2.destroyAllWindows()


cv2.cvtColor([[[255, 0, 0]]], cv2.COLOR_BGR2HSV)
"""

import pyautogui
from scipy.spatial import KDTree
import webcolors

"""
def convert_rgb_to_names(rgb_tuple):
    
    # a dictionary of all the hex and their respective names in css3
    css3_db = css3_hex_to_names
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return f'closest match: {names[index]}'
"""

while True:
    x, y = pyautogui.position()
    px = pyautogui.pixel(x, y)
    named_color = print(rgb_to_name(px))
    print(named_color)