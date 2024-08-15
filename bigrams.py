from collections import Counter
import re
from nltk import bigrams
from nltk.corpus import stopwords
import nltk

import pandas as pd
import matplotlib.pyplot as plt
import json

# Load the JSON file
file_path_json = 'anpuh13-23.json'
with open(file_path_json, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Create a DataFrame from the JSON data
df = pd.DataFrame(data)

# Convert all text to lowercase for case-insensitive search
df['Resumo'] = df['Resumo'].str.lower()

# Search for the term "história da educação" in the "Resumo" column
df['contains_historia_da_educacao'] = df['Resumo'].str.contains('história da educação')

# Count the occurrences by year
historia_da_educacao_by_year = df.groupby('Ano')['contains_historia_da_educacao'].sum().reset_index()

# Count the occurrences by ST (Simposio Temático)
historia_da_educacao_by_st = df[df['contains_historia_da_educacao']].groupby('ST').size().reset_index(name='count')

# Sort the ST occurrences in descending order
historia_da_educacao_by_st_sorted = historia_da_educacao_by_st.sort_values(by='count', ascending=False)

# Ensure that the necessary NLTK resources are downloaded
nltk.download('stopwords')

# Define Portuguese stop words
stop_words = set(stopwords.words('portuguese'))

# Filter the DataFrame to include only rows with "história da educação" in the "Resumo"
filtered_df = df[df['contains_historia_da_educacao']]

# Combine all the relevant text into a single string
all_resumo_text = ' '.join(filtered_df['Resumo'])

# Remove punctuation and split the text into words
words = re.findall(r'\b\w+\b', all_resumo_text)

# Remove stop words from the list of words
filtered_words = [word for word in words if word not in stop_words]

# Generate bigrams
bigrams_list = list(bigrams(filtered_words))

# Count the frequency of each bigram
bigram_counts = Counter(bigrams_list)

# Display the most common bigrams
common_bigrams = bigram_counts.most_common(50)  # Getting the 50 most common bigrams
common_bigrams

if common_bigrams:
    print(common_bigrams)
else:
    print("No common bigrams found.")
