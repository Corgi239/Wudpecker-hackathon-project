# print current working directory
import os
print(os.getcwd())

from src.data_processor import DataProcessor

data_path = './data/raw/'
dp = DataProcessor(data_path=data_path)
df = dp.get_data
print(df)
print(df.info())
