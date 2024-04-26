from src.CnnClassifier.config.configuration import ConfigurationManager
from src.CnnClassifier.components.prepare_base_model import PrepareBaseModel
from src.CnnClassifier import logger
from src.CnnClassifier.logger.logg import logging


class PreparebaseModel:
     def __init__(self):
          pass
     
     def main(self):
          try:
               config=ConfigurationManager()
               prepare_base_model_config=config.get_prepare_base_model_config()
               prepare_base_model=PrepareBaseModel(config=prepare_base_model_config)
               prepare_base_model.get_base_model()
               prepare_base_model.update_base_model()
          except Exception as e:
               raise(e)
          


