from pathlib import Path
import cv2 
 

class VideoSource:
  def __init__(self, folder_path, extension=".jpg"):
    self.folder_path = Path(folder_path)
    self.frame_paths = sorted(self.folder_path.glob(f"*{extension}"))
    if len(self.frame_paths) == 0:
      raise ValueError(f"No {extension} found in {folder_path}")

  def frames(self):
    for i,path in enumerate(self.frame_paths):
      frame = cv2.imread(str(path))
      if frame is None:
        raise ValueError(f"Could not read {path}")
      yield i, frame

    