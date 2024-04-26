import os 
import urllib.request as request
import zipfile
from src.CnnClassifier.logger.logg import logging
from src.CnnClassifier.utils.common import get_size
from src.CnnClassifier.config.configuration import ConfigurationManager
from src.CnnClassifier.entity.config_entity import DataIngestionConfig
class DataIngestion:
     def __init__(self,config:DataIngestionConfig):
          self.config=config
          
     def download_file(self):
          if not os.path.exists(self.config.local_data_file):
               filename,headers=request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
               )
               file_path = Path(self.config.local_data_file)
               logging.info(f"Downloaded {get_size(file_path)} from {self.config.source_URL}")
          else:
               logging.info(f"{self.config.local_data_file} already exists")
               
     def extract_zip_file(self):
          unzip_path=self.config.unzip_dir
          os.makedirs(unzip_path,exist_ok=True)
          with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
               zip_ref.extractall(unzip_path)
               logging.info(f"Extracted {self.config.local_data_file} to {self.config.unzip_dir}")