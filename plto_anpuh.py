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

# Create a bar chart for the occurrences by year
plt.figure(figsize=(10, 6))
plt.bar(historia_da_educacao_by_year['Ano'], historia_da_educacao_by_year['contains_historia_da_educacao'], color='blue')
plt.xlabel('Ano')
plt.ylabel('Ocorrências')
plt.title('Ocorrências do tema "História da Educação" nos Resumos por Ano')
plt.xticks(historia_da_educacao_by_year['Ano'])
plt.grid(True)
plt.show()

# Create a bar chart for the occurrences by ST show only the 10 most frequent ST
plt.figure(figsize=(12, 8))
plt.bar(historia_da_educacao_by_st_sorted['ST'][:10], historia_da_educacao_by_st_sorted['count'][:10], color='green')
plt.xlabel('Simposio Temático')
plt.ylabel('Ocorrências')
plt.title('Ocorrências do tema "História da Educação" nos Resumos por Simposio Temático')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

