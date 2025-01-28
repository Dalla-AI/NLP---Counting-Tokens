import argparse
import re
from collections import Counter
import matplotlib.pyplot as plt
import nltk
import numpy as np
import os

nltk.download('stopwords')
nltk.download('wordnet')

def load_text(file_path):
    """Load text from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def normalize_text(text, lower=True, remove_stopwords=True, stem=False, lemmatize=False, min_word_count=1):
    """Normalize the text based on user options."""
    # Lowercase text
    if lower:
        text = text.lower()

    # Tokenize text
    tokens = re.findall(r'\b\w+\b', text)

    # Remove stopwords
    if remove_stopwords:
        stop_words = set(nltk.corpus.stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]

    # Stemming or Lemmatization
    if stem:
        stemmer = nltk.PorterStemmer()
        tokens = [stemmer.stem(token) for token in tokens]
    elif lemmatize:
        lemmatizer = nltk.WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return tokens

def count_tokens(tokens, min_word_count):
    """Count the frequency of each token and filter by minimum word count."""
    token_counts = Counter(tokens)
    filtered_counts = {token: count for token, count in token_counts.items() if count > min_word_count}
    return Counter(filtered_counts)

def save_and_plot_counts(counts, output_file):
    """Save token counts and generate a visualization."""
    # Sort counts
    sorted_counts = counts.most_common()

    # Save to file
    with open(output_file, 'w') as f:
        for token, count in sorted_counts:
            f.write(f"{token} {count}\n")

    # Prepare data for visualization
    ranks = np.arange(1, len(sorted_counts) + 1)
    frequencies = [count for _, count in sorted_counts]

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(ranks, frequencies, marker='o', linestyle='-', markersize=3)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Token Frequency Distribution')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig(output_file.replace('.txt', '.png'))
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Normalize text and count tokens.")
    parser.add_argument('file', type=str, help="Path to the input text file.")
    parser.add_argument('--lower', action='store_true', help="Lowercase the text.")
    parser.add_argument('--stem', action='store_true', help="Apply stemming to the tokens.")
    parser.add_argument('--lemmatize', action='store_true', help="Apply lemmatization to the tokens.")
    parser.add_argument('--remove_stopwords', action='store_true', help="Remove stopwords from the text.")
    parser.add_argument('--min_word_count', type=int, default=1, help="Minimum count of words to include in the output.")
    parser.add_argument('--output', type=str, default='token_counts.txt', help="Path to save token counts.")

    args = parser.parse_args()

    # Ensure only one of stem or lemmatize is used
    if args.stem and args.lemmatize:
        raise ValueError("You cannot use both stemming and lemmatization at the same time.")

    # Load text
    text = load_text(args.file)

    # Normalize text
    tokens = normalize_text(
        text,
        lower=args.lower,
        remove_stopwords=args.remove_stopwords,
        stem=args.stem,
        lemmatize=args.lemmatize
    )

    # Count tokens with minimum word count filtering
    counts = count_tokens(tokens, args.min_word_count)

    # Save counts and plot
    save_and_plot_counts(counts, args.output)

if __name__ == "__main__":
    main()
