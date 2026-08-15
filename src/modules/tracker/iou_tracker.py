from src.core.base_module import BaseModule
from src.core.datatypes import Track

def iou(box_a, box_b):
  x1 = max(box_a[0], box_b[0])
  y1 = max(box_a[1], box_b[1])

  x2 = min(box_a[2], box_b[2])
  y2 = min(box_a[3], box_b[3])

  width = max(0, x2- x1)
  height = max(0,y2 - y1)

  overlapping_area = width * height
  area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
  area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
  union = area_a + area_b - overlapping_area
  return 0.0 if union == 0 else overlapping_area / union



class IouTracker(BaseModule):
  def __init__(self, iou_threshold=0.3,max_age=5):
    self.iou_threshold = iou_threshold
    self.max_age = max_age
    self.tracks = []
    self.next_id = 0

print(iou((0, 0, 10, 10), (0, 0, 10, 10)))    # 1.0  identical
print(iou((0, 0, 10, 10), (20, 0, 30, 10)))   # 0.0   
print(iou((0, 0, 10, 10), (0, 20, 10, 30)))   # 0.0   
print(iou((0, 0, 10, 10), (5, 5, 15, 15)))    # 0.1428