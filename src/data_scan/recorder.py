import csv
from pathlib import Path
from src.core.base_module import BaseModule

class CsvRecorder(BaseModule):
  def __init__(self, output_dir="results"):
    self.output_dir = Path(output_dir)
    self.output_dir.mkdir(parents=True,exist_ok=True)

    self.predictions_file = open(self.output_dir / "predictions.csv", "w", newline="")
    self.positions_file = open(self.output_dir / "positions.csv", "w", newline="")

    self.predictions_writer = csv.writer(self.predictions_file)
    self.positions_writer = csv.writer(self.positions_file)

    self.predictions_writer.writerow(["frame_id", "track_id", "horizon", "pred_x", "pred_y"])
    self.positions_writer.writerow(["frame_id", "track_id", "x", "y"])

  def process(self, state):
    for track in state.tracks:
      x,y = track.last_detection.center
      self.positions_writer.writerow([state.frame_id,track.track_id,x,y])

    for prediction in state.predictions:
      self.predictions_writer.writerow([
      prediction.frame_id,
      prediction.track_id,
      prediction.horizon,
      prediction.point[0],
      prediction.point[1],
      ])

  def finish(self):
    self.predictions_file.close()
    self.positions_file.close()