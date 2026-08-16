
from src.core.datatypes import PipelineState

class Coordinator:
  def __init__(self, modules):
    self.modules = modules


  def run(self, source, max_frames=None):
    for frame_id, frame in source.frames():
      state = PipelineState(frame_id, frame)
      
      for module in self.modules:
        module.process(state)
        
      if max_frames is not None and max_frames <= frame_id + 1:
        break

      print(f"frame {frame_id}: {len(state.detections)} det, {len(state.tracks)} tracks, {len(state.predictions)} predictions")

    for module in self.modules:
      module.finish()
