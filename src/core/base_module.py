from src.core.datatypes import PipelineState


#abstract
class BaseModule:

  def process(self, state:PipelineState):
    raise NotImplementedError