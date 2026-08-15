

from src.core.base_module import BaseModule
from src.core.datatypes import Prediction





class ConstantVelocityPredictor(BaseModule):
  def __init__(self, window=5, horizons=(5,15,30)):
    self.window = window
    self.horizons = horizons

  def process(self, state):
    for track in state.tracks:
      history = track.history
      if len(history) < self.window +1:
        continue

      current = track.last_detection
      past = track.history[-1 - self.window]

      cx,cy = current.center
      px,py = past.center
      frame_gap = current.frame_id - past.frame_id
      if frame_gap == 0: continue

      velocity_x = (cx-px) / frame_gap 
      velocity_y = (cy - py) / frame_gap

      for horizon in self.horizons:
        prediction_point =  (cx + velocity_x * horizon, cy + velocity_y * horizon)
        prediction = Prediction(track_id=track.track_id, frame_id=state.frame_id, horizon=horizon, point=prediction_point)
        state.predictions.append(prediction)