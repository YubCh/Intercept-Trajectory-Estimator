import argparse
from src.data_scan.video_source import VideoSource
from src.data_scan.visualizer import DetectionVisualizer
from src.modules.detector.yolo_detector import YoloDetector
from src.core.coordinator import Coordinator
from src.modules.tracker.iou_tracker import IouTracker
from src.modules.predictor.constant_velocity import ConstantVelocityPredictor
from src.data_scan.recorder import CsvRecorder
def main():
    parser = argparse.ArgumentParser(description="Run Detections on VisDrone sequence")
    parser.add_argument("--sequence", required=True, help="Path to sequence folder")
    parser.add_argument("--output", default="outputs", help="Where to write the output")
    parser.add_argument("--max-frames",type=int,default=None,help="Stopping after N frames")
    args = parser.parse_args()

######DETECTION

    source = VideoSource(args.sequence)
    detector = YoloDetector()
    visualizer = DetectionVisualizer(args.output)
    recorder = CsvRecorder()
    tracker = IouTracker()
    predictor = ConstantVelocityPredictor()
    coordinator = Coordinator([detector, tracker,predictor, visualizer,recorder])
    coordinator.run(source, max_frames=args.max_frames)
    
######TRACKING
    

if __name__ == "__main__":
    main()