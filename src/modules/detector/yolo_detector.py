
from ultralytics import YOLO
from src.core.base_module import BaseModule
from src.core.datatypes import Detection, PipelineState


class YoloDetector(BaseModule):
  def __init__(self,model_name="yolov8m.pt", conf_treshhold = 0.25,allowed_classes = None):
    self.conf_treshold = conf_treshhold
    self.model = YOLO(model_name)
    self.allowed_classes = allowed_classes

  def process(self, state):
    results = self.model(state.frame, verbose=False)
    for box in results[0].boxes:
      confidence = box.conf[0].item()
      if confidence < self.conf_treshold:
        continue
 
      class_id = int(box.cls[0].item())
      class_name = self.model.names[class_id]
      if self.allowed_classes is not None and class_name not in self.allowed_classes:
        continue

      bbox = tuple(box.xyxy[0].tolist())
      dec = Detection(bbox,confidence,class_id,class_name,state.frame_id)
      state.detections.append(dec)