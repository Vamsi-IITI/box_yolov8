#!/usr/bin/env python3
import cv2
import os
from ultralytics import YOLO

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)


# Load the YOLOv8 model
model = YOLO('best.pt')

# Open the video file
videoFilePath = "box.mp4"
videoFile = cv2.VideoCapture(videoFilePath)

# Get video properties
frame_width = int(videoFile.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(videoFile.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the output video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 1, (frame_width, frame_height))                       ## Though there is some issue with video saving. Not fixed

# Process frames in the video
unique_id = set()

while videoFile.isOpened():
    success, frame = videoFile.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model.track(frame, tracker="bytetrack.yaml") 
        img = results[0].plot()
        height, width, _ = img.shape

        if results[0].boxes.id is not None:
            boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
            ids = results[0].boxes.id.cpu().numpy().astype(int)
            for box, id in zip(boxes, ids):
                int_id = int(id)
                if int_id not in unique_id:
                    unique_id.add(int_id)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

            cv2.line(img, (width - 500, 25), (width, 25), [85, 45, 255], 40)
            cv2.putText(img, f'Number of boxes: {len(unique_id)}', (width - 500, 35), 0, 1, [225, 255, 255], thickness=2, lineType=cv2.LINE_AA)
            resized_img = ResizeWithAspectRatio(img, width=720)
            cv2.imshow('Detected Frame', resized_img)
            print(len(unique_id))

            out.write(resized_img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Release the video capture and video writer objects
videoFile.release()
out.release()

cv2.destroyAllWindows()
