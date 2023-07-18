# box_yolov8
Yolo v8s (Small) model for box detection.

## Instructions for use
* Clone the repository
```
git clone https://github.com/Vamsi-IITI/box_yolov8.git
```
* Place test images in folder box_yolov8/test/images
* Run
```
yolo task=detect mode=predict model=~/box_yolov8/best.pt conf=0.25 source=~/box_yolov8/test/images save=True
```

### For detection in image
* Use count.py . Run
```
python3 count.py
```
### For object detection and tracking in video
* Use track.py . Run
```
python3 track.py
```

#### Note :
Both track_and_video_save.py and box_detection_ros.py have some issues currently

## Few Results : 

![two_boxes](https://github.com/Vamsi-IITI/box_yolov8/assets/92263050/17a33ebf-0835-45b2-ad3f-c3faf82b9e24)

![cardboardbox](https://github.com/Vamsi-IITI/box_yolov8/assets/92263050/7246bf23-5832-435e-b12a-42d18d06e0c2)
