import numpy as np
from dataclasses import dataclass
from dataclasses import dataclass, field
@dataclass
class Detection:
  bbox: tuple[float, float, float, float]
  confidence: float
  class_id: int
  class_name: str
  frame_id: int

  @property
  def center(self) -> tuple[float,float]:
    x1,y1,x2,y2 = self.bbox
    return (x1+x2) / 2 , (y1+y2) / 2

@dataclass
class Pipleinestate:
  frame_id:int
  image: np.ndarry
  detections: list[Detection] = field(default_factory=list)