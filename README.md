# NLP---Counting-Tokens
Simple python project for text normalization and analysis, with token frequency counting and customizable preprocessing options.

## Overview
This project processes natural language text files to:
- Normalize text (lowercasing, lemmatization, stemming, stopword removal, & min word count).
- Count token frequencies with customizable options.
- Visualize word frequency distributions.

## Features
- Customizable preprocessing:
- Lowercasing, stopword removal, stemming, lemmatization.
- Filter tokens by minimum frequency.
- Generates token frequency visualizations.

## Normalize Text and Token Counter Usage
1. Clone the repository:
   
   ````
   git clone https://github.com/dalla-AI/text-normalization-project.git
   ````
   ````
   cd text-normalization-project
   ````
   
2. Install dependencies:
   
   ````
   pip install -r requirements.txt
   ````
   
3. Run the program:
   

      For Token Counter:
   
         
   Load "normalize_text.py" in your prefered IDE. Source "The Wonderful Wizard of OZ.txt" in the same directory and run program.
         

      For Text Normalization:
   
         
         python src/normalize_text.py data/input/example_text.txt --lower --lemmatize --remove_stopwords --min_word_count 2 --output data/output/token_counts.txt
         
   
   (Edit min word count above of your choosing ex. 1, 2, 3, 4, etc.)
   
View results in data/output/
