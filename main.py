from src.CnnClassifier.logger.logg import logging
from src.CnnClassifier.pipeline.model_eval_pipeline import EvalutionPipeline
from src.CnnClassifier.pipeline.model_train import TrainingPipeline
from src.CnnClassifier.pipeline.prepare_callbacks_03 import \
    PrepareCallbacksPipeline
from src.CnnClassifier.pipeline.preparebase_model_02 import \
    PreparebaseModelPipeline
from src.CnnClassifier.pipeline.stage_01_data_ingestion import \
    DataINgestionPipeline

if __name__ == '__main__':
     try:
          obj=DataINgestionPipeline()
          logging.info("Enter into the data ingestion from github method")
          obj.main()
          obj2=PreparebaseModelPipeline()
          logging.info("Enter into the base model method to assign the base model")
          obj2.main()
          obj3=PrepareCallbacksPipeline()
          obj3.main()
          obj4=TrainingPipeline()
          obj4.main()
          obj5=EvalutionPipeline()
          obj5.main()
     except Exception as e:
          logging.info(e)