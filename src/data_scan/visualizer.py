
import cv2

from pathlib import Path
from src.core.base_module import BaseModule



BOX_COLOR = (0, 255, 0)


class DetectionVisualizer(BaseModule):
  def __init__(self, output_dir="outputs",trail_length=30):
    self.output_dir = Path(output_dir)
    self.output_dir.mkdir(parents=True, exist_ok=True)
    self.trail_length = trail_length

  def process(self, state):
    annotated = state.frame.copy()

    for track in state.tracks:
      detection = track.last_detection
      x1,y1,x2,y2 = (int(v) for v in detection.bbox)

      cv2.rectangle(annotated, (x1,y1), (x2,y2), BOX_COLOR, 2)

      label = f"#{track.track_id} {detection.class_name}"

      cv2.putText(
        annotated, label, (x1, y1 - 5), cv2.FONT_HERSHEY_COMPLEX, 0.5, BOX_COLOR, 2,
      )
      trail_points = [detection.center for detection in track.history[-self.trail_length:]]

      for start, end in zip(trail_points, trail_points[1:]):
        cv2.line(annotated, tuple(int(v) for v in start),tuple(int(v) for v in end), BOX_COLOR,1)
    cv2.imwrite(str(self.output_dir/f"{state.frame_id}.jpg"), annotated)

