"""
This is the main file for the project.
"""

import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

from src.data_processor import DataProcessor
from src.n_grams_scorer import NGramsScorer


class Document(BaseModel):
    text: str


def get_transcripts(data_path):
    processor = DataProcessor(data_path=data_path)
    df = processor.get_data
    df.reset_index(inplace=True)
    return df


def train_test_split(transcripts_df):
    # Select a portion of good transcripts for training
    good_transcripts = transcripts_df[transcripts_df.meaningful == 1.0]["content"]
    bad_transcripts = transcripts_df[transcripts_df.meaningful == 0.0]["content"]

    n_good = good_transcripts.shape[0]
    n_bad = bad_transcripts.shape[0]

    n_training = n_good - n_bad
    training_ind = np.random.choice(range(n_good), size=n_training, replace=False)
    testing_ind = [i for i in range(n_bad + n_good) if i not in training_ind]
    training_data = good_transcripts[training_ind].values
    testing_data = transcripts_df.loc[testing_ind, "content"].values
    testing_labels = transcripts_df.loc[testing_ind, "meaningful"].values

    return training_data, testing_data, testing_labels


# Initialize scorer and fit to training data
scorer = NGramsScorer()
transcripts_df = get_transcripts("./data/raw/")
training_data, testing_data, testing_labels = train_test_split(transcripts_df)
scorer.fit(training_data)

# Compute training scores and descriptive statistics of scores
training_scores = [scorer.score(text) for text in training_data]
df_train_score = pd.DataFrame(np.array(training_scores))
train_stats = df_train_score.describe().to_dict()[0]


# Create FastAPI app and define endpoints
app = FastAPI()


@app.get("/")
async def root():
    # Include training scores and statistics in the response
    response_data = {
        "training descriptive statistics": train_stats,
        "training scores": df_train_score[0].tolist(),
    }
    return response_data


@app.post("/score/")
async def score_item(document: Document):
    text = document.text
    score = scorer.score(text)

    response_data = {
        "training descriptive statistics": train_stats,
        "cohesive scores for text": score,
    }

    return response_data
