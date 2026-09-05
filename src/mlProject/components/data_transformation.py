import os
import pandas as pd
from sklearn.model_selection import train_test_split
from mlProject import logger
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Handle missing values & categorical columns
        data = data.dropna()
        data = pd.get_dummies(data, columns=['ocean_proximity'], drop_first=True)

        train, test = train_test_split(data, test_size=0.25, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(f"Train shape: {train.shape}, Test shape: {test.shape}")