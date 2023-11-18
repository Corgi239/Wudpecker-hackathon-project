import pandas as pd
import os
import json


class DataProcessor:
    def __init__(self, 
                 *, 
                 data_path: str
        ) -> None:
        self.data_path = data_path
        self.data = self.__get_clean_data()
    
    @property
    def get_data(self) -> pd.DataFrame:
        return self.data
    

    def __get_clean_data(self) -> pd.DataFrame:
        df = pd.concat([self.__get_good_data(), self.__get_bad_data()])
        return df
    

    def __get_good_data(self) -> pd.DataFrame:
        folder_key = 'transcripts'
        df = self.__get_raw_data(folder_key)
        df['meaningful'] = 1
        return df
    

    def __get_bad_data(self) -> pd.DataFrame:
        folder_key = 'wrong_langs'
        df = self.__get_raw_data(folder_key)
        df['meaningful'] = 0
        return df


    def __get_raw_data(self, folder_key: str) -> pd.DataFrame:
        data_path = self.data_path + folder_key + '/'
        df = self.__read_jsons(data_path)
        return df


    def __read_jsons(self, data_path: str) -> pd.DataFrame:
        transcript_files = [pos_json for pos_json in os.listdir(data_path) if pos_json.endswith('.json')]

        contents = []
        for file_name in transcript_files:
            file_path = data_path + file_name
            with open(file_path) as file_content:
                data = json.load(file_content)
                text = data['results']['transcripts'][0]['transcript']
                contents.append(text)

        df = pd.DataFrame({'file_name': transcript_files, 'content' : contents})
        df.set_index('file_name', inplace=True)
        return df        
