from dataclasses import dataclass

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

d = Detection((10, 20, 50, 80), 0.87, 2, "car", 14)
print(d.center)