import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'show_id': ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8'],
    'title': ['Breaking Bad', 'The Crown', 'Stranger Things', 'DARK', 'Narcos', 'The Office', 'Friends', 'The Witcher'],
    'type': ['TV Show', 'TV Show', 'TV Show', 'TV Show', 'TV Show', 'TV Show', 'TV Show', 'TV Show'],
    'release_year': [2008, 2016, 2016, 2017, 2015, 2005, 1994, 2019],
    'country': ['United States', 'United Kingdom', 'United States', 'Germany', 'Colombia', 'United States', 'United States', 'Poland'],
}

df = pd.DataFrame(data)
print(f"Total: {len(df)}")
print(df['type'].value_counts())
print(df['country'].value_counts())
