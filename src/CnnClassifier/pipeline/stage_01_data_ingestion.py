from src.CnnClassifier.config.configuration import ConfigurationManager
from src.CnnClassifier.components.data_ingestion import DataIngestion
from src.CnnClassifier import logger
from src.CnnClassifier.logger.logg import logging


class DataINgestionPipeline:
     def __init__(self):
          pass
     
     def main(self):
          try:
               config=ConfigurationManager()
               data_ingestion_config=config.get_data_ingestion_config()
               dataingestion=DataIngestion(data_ingestion_config)
               dataingestion.download_file()
               dataingestion.extract_zip_file()
          except Exception as e:
               raise(e)
          


