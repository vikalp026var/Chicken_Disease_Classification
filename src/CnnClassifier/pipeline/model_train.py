from src.CnnClassifier.config.configuration import ConfigurationManager
from src.CnnClassifier.components.model_train import Training
from src.CnnClassifier.components.prepare_callbacks_03 import PrepareCallback
# from src.CnnClassifier import logger
from src.CnnClassifier.logger.logg import logging


class TrainingPipeline:
     def __init__(self):
          pass
     
     def main(self):
          try:
               config = ConfigurationManager()
               prepare_callbacks_config = config.get_prepare_callback_config()
               prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
               callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

               training_config = config.get_training_config()
               training = Training(config=training_config)
               training.get_base_model()
               training.train_valid_generator()
               training.train(
                    callback_list=callback_list
               )
               
          except Exception as e:
               raise e
          


