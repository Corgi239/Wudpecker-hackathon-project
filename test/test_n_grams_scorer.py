import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_processor import DataProcessor
from src.n_grams_scorer import NGramsScorer

data_path = './data/raw/'
dp = DataProcessor(data_path=data_path)
df = dp.get_data

transcripts_df = df.copy()

# selecting a portion of good transcripts for training
good_transcripts = transcripts_df[transcripts_df.meaningful == 1.0]['content']
bad_transcripts  = transcripts_df[transcripts_df.meaningful == 0.0]['content']

n_good  = good_transcripts.shape[0]
n_bad   = bad_transcripts.shape[0]

n_training = n_good - n_bad
training_ind = np.random.choice(range(n_good), size=n_training, replace=False)
testing_ind = [i for i in range(n_bad + n_good) if i not in training_ind]
training_data = good_transcripts[training_ind].values
testing_data = transcripts_df.loc[testing_ind, 'content'].values
testing_labels = transcripts_df.loc[testing_ind, 'meaningful'].values

scorer = NGramsScorer()
scorer.fit(training_data)
testing_scores = [scorer.score(text) for text in testing_data]