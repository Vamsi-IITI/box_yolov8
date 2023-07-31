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
* Use track.py . Mention the video in the code. Run
```
python3 track.py
```
https://github.com/Vamsi-IITI/box_yolov8/assets/92263050/3b75b0f1-4bdf-4bf9-b2d3-9342ab0a3635

[Video Demo](https://drive.google.com/file/d/1Fjsb6AEO1Riwbcl14Lf_UojTIClW0W91/view)

#### Note :
Both track_and_video_save.py and box_detection_ros.py have some issues currently

## Training Results :
![image](https://github.com/Vamsi-IITI/box_yolov8/assets/92263050/4001ba25-375d-49b9-b22a-c561426cfe41)


## Few Results : 

![two_boxes](https://github.com/Vamsi-IITI/box_yolov8/assets/92263050/17a33ebf-0835-45b2-ad3f-c3faf82b9e24)

![cardboardbox](https://github.com/Vamsi-IITI/box_yolov8/assets/92263050/7246bf23-5832-435e-b12a-42d18d06e0c2)

![image](https://github.com/Vamsi-IITI/box_yolov8/assets/92263050/59bd90fd-46cb-4a13-b668-376222959f87)

