import math

def calculateAngle(p1, p2, p3):
    x1, y1, _ = p1
    x2, y2, _ = p2
    x3, y3, _ = p3

    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    if angle < 0:
        angle += 360
    return angle