from text_summarizer.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.logging import logger 
from text_summarizer.pipelines.stage_02_data_validation import DataValidationTrainingPipeline
from text_summarizer.pipelines.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = 'Data Validation stage'

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = 'Data Tranfomation stage'

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataTransformationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed!<<<<<")
except Exception as e:
    logger.exception(e)
    raise e 
