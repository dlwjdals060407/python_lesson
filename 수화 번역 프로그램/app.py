import cv2
import mediapipe as mp
import math

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
my_hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

def dist(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2,2)) + math.sqrt(math.pow(y1 - y2,2))

compareIndex = [[18,4], [6,8], [10,12], [14,16], [18.20]]
open = [False,False,False,False,False]
gesture = [[True, True, True, True, True, "Hi"],
           [False, False, False, False, False,"yeah"],
           [True, True, False, False, True, "!!"]]

while True:
    success, ima