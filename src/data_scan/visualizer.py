
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

    