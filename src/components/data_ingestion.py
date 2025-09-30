import os
import sys

from src.components.data_transformation import DataTransformation
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def intiate_data_ingestion(self):
        logging.info("Entered The data ingestion method or component")
        try:
            df= pd.read_csv("notebook\data\stud.csv")
            logging.info("Reading dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train Test Split initiated")
            train, test = train_test_split(df, test_size=.2, random_state=42)
            train.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == '__main__':
    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.intiate_data_ingestion()

    data_transform = DataTransformation()
    data_transform.initiate_data_transformation(train_data_path, test_data_path)




