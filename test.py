import cv2

for i in range(10): # デバイスIDを0から9まで試す
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera found at index: {i}")
        cap.release()
    else:
        print(f"No camera found at index: {i}")
