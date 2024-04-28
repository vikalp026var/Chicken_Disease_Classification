from src.CnnClassifier.config.configuration import ConfigurationManager
from src.CnnClassifier.components.model_evaluation import Evaluation
# from src.CnnClassifier.components.prepare_callbacks_03 import PrepareCallback
# from src.CnnClassifier import logger
from src.CnnClassifier.logger.logg import logging


class EvalutionPipeline:
     def __init__(self):
          pass
     
     def main(self):
          try:
               config = ConfigurationManager()
               val_config = config.get_validation_config()
               evaluation = Evaluation(val_config)
               evaluation.evaluation()
               evaluation.save_score()

          except Exception as e:
               raise e
          


