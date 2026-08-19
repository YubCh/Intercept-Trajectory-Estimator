# Multi Target Motion Tracking & Intercept Trajectory Estimator

A modern perception pipeline that detects objects in aerial video, tracks them with persistent identities across frames, and estimates where they will be several frames into the future. 

Built on VisDrone2019-MOT — drone footage of road scenes, annotated for multi-object tracking.



# What it does so far
![Frame 1](outputs/uav0000339/1.jpg)
![Frame 12](outputs/uav0000339/12.jpg)
![Frame 29](outputs/uav0000339/29.jpg)
<!-- TODO: find right picture demonstrating the project  -->
# Architecture
![Classes_uml](results/classes.png)
![Classes_uml](results/datatypes.png)
<!-- TODO: try to recreate uml in digital format  -->
## Data types
## Key Methods
<!-- TODO: describe each module  -->
- Detection:
- Tracking:
- Prediction:


# Project Structure
```text
scripts/
  - run_pipeline.py
src/
  core/
    - base_module.py
    - coordinator.py
    - datatypes.py
  data_scan/
    - recorder.py
    - video_source.py
    - visualizer.py
  module/
    detector/
      - yolo_detector.py
    predictor/
      - constant_velocity.py
    tracker/
      - iou_tracker.py
    intercept/ # not written yet
```

# How to Run
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python -m scripts.run_pipeline --sequence data/visdrone/VisDrone2019-MOT-val/sequences/uav0000339_00001_v
python -m scripts.evaluate
```

# What has to be fixed
<!-- TODO: pick out images that contain our problems  -->
![Frame 30](outputs/uav0000339/30.jpg)
Frame 30
![Frame 36](outputs/uav0000339/36.jpg)
Frame 36

We can see a sudden change in our tracking which is caused by the sudden drop of the drone view. The tracking does not calculate the movement of the camera itself which leads to a sudden change of the position



# Tech Stack

# Data sources & acknowledgements
- VisDrone dataset — aerial imagery used throughout this project. Provided by the AISKYEYE team at the Lab of Machine Learning and Data Mining, Tianjin University. Project: https://github.com/VisDrone/VisDrone-Dataset