from dataclasses import dataclass
from pathlib import Path
from src.CnnClassifier.logger.logg import logging

@dataclass(frozen=True)
class DataIngestionConfig:
     root_dir: Path 
     source_URL: Path 
     local_data_file: Path 
     unzip_dir: Path 
     
@dataclass(frozen=True)
class PrepareBaseMOdelConfig:
     root_dir: Path 
     base_model_path: Path 
     updated_base_model_path: Path 
     params_image_size: list 
     params_learning_rate: float
     params_include_top: bool 
     params_weights: str 
     params_classes: int 
     
     
@dataclass(frozen=True)
class PrepareCallbacksConfig:
    logging.info('Prepare call backs config entity ')
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path
    
    
@dataclass(frozen=True)
class TrainingConfig:
     logging.info("Enter into training config entity")
     root_dir: Path 
     trained_model_path: Path 
     updated_base_model_path: Path 
     training_data: Path 
     params_epochs: int 
     params_batch_size: int
     params_is_augmentation: bool
     params_image_size: list
     


@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    params_image_size: list
    params_batch_size: int
    