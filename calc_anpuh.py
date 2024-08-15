import pandas as pd
import json

# Load the JSON file
file_path_json = 'anpuh13-23.json'  # Substitua pelo caminho do seu arquivo JSON
with open(file_path_json, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Create a DataFrame from the JSON data
df = pd.DataFrame(data)

# Convert all text to lowercase for case-insensitive search
df['Resumo'] = df['Resumo'].str.lower()

# Search for the term "história da educação" in the "Resumo" column
df['contains_historia_da_educacao'] = df['Resumo'].str.contains('história da educação')

# Total number of summaries in the ANPUH dataset
total_resumos = df.shape[0]

# Total number of occurrences for "história da educação"
total_occurrences_historia_educacao = df['contains_historia_da_educacao'].sum()

# Calculate the proportion of occurrences by year
proportion_by_year = df.groupby('Ano')['contains_historia_da_educacao'].mean().reset_index()

# Print the results
print(f"Total de resumos na base ANPUH: {total_resumos}")
print(f"Total de ocorrências de 'história da educação': {total_occurrences_historia_educacao}")

# Print the proportion of occurrences by year
print("\nProporção de ocorrências por ano:")
print(proportion_by_year)
