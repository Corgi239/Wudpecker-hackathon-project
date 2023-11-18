[![Python application test with Github Actions](https://github.com/Corgi239/Wudpecker-hackathon-project/actions/workflows/devops.yml/badge.svg)](https://github.com/Corgi239/Wudpecker-hackathon-project/actions/workflows/devops.yml)

# Wudpecker-hackathon-project

Text classification microservice prepared for the 2023 Wudpecker AI hackathon. The primary goal of the service is early detection of heavily corrupted transcripts (for instance, due to incorrectly recognized language), before they are sent down the pipeline for summarization. 

## Usage

## Method

While exploring the provided sample data, we observed that in corrupted transcripts, consecutive words often appear semantically disconnected from each other, while in correctly transcribed conversations, consecutive words typically make sense together. We leveraged this observation to construct a scoring metric that differentiates nonsensical transcripts from ones that accurately transcribe the original conversation.

The steps for calculating the metric are roughly as follows:
1. First, we gather a corpus of verified transcripts to be used as training material. This data could be formed from a collection of various transcripts in Wudpecker's possession, or gathered from among texts produced by the specifically by the client to preserve confidentiality and improve customizability.
2. We then tokenize the texts and divide them into bigrams (pairs of consecutive tokens). The resulting bigram counts are stored in an instance of the `NgramCounter` class from the `nltk` package. 
3. At testing time, we tokenize the text to be tested and similarly divide it into bigrams. Then, for each resulting bigram, we calculate the frequency of that bigram within the training corpus, compared to the frequencies of those bigram with the same first token. For instance, when if we encounter a bigram "fluffy dog" in the tested text, we will count how many times "fluffy dog" appears in the training corpus, and divide by the total appearance count of the word "fluffy" in that corpus. The resulting value represents the likelihood of the encountered bigram appearing given the training texts as a statistical model.
4. Finally, we use the mean of the resulting ratios as the final score. 

## Create scaffold structure for project

1. Create a Python virtual environment `python3 -m venv myenv`
2. Create empty files for project structure: `Makefile`, `requirements.txt`, `main.py`, `Dockerfile`, `src/`
3. Populate `Makefile`
4. Set up continuous integration with Github Workflow: automatic linting, testing, formatting, building, etc
