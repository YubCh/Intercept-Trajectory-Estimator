
import cv2

from pathlib import Path
from src.core.base_module import BaseModule



BOX_COLOR = (0, 255, 0)


class DetectionVisualizer(BaseModule):
  def __init__(self, output_dir="outputs"):
    self.output_dir = Path(output_dir)
    self.output_dir.mkdir(parents=True, exist_ok=True)

  def process(self, state):
    annotated = state.frame.copy()

    for detection in state.detections:
      x1,y1,x2,y2 = (int(v) for v in detection.bbox)

      cv2.rectangle(annotated, (x1,y1), (x2,y2), BOX_COLOR, 2)

      label = f"{detection.class_name} {detection.confidence:.2f}"

      cv2.putText(
        annotated, label, (x1, y1 - 5), cv2.FONT_HERSHEY_COMPLEX, 0.5, BOX_COLOR, 2,
      )
    cv2.imwrite(str(self.output_dir/f"{state.frame_id}.jpg"), annotated)