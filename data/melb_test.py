import pandas as pd
from IPython.display import display
melb_df = pd.read_csv('data/melb_data.csv', sep=',')
unique_list = []
for col in melb_df.columns:
    item = (col, melb_df[col].nunique(),melb_df[col].dtype)
    unique_list.append(item)
unique_counts = pd.DataFrame(
    unique_list,
    columns = ['Column_Name', 'Num_Unique', 'Type']
).sort_values(by = 'Num_Unique', ignore_index = True)
display(unique_counts)
display(melb_df.info())
cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']
max_unique_count = 150
for col in melb_df.columns:
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude:
        melb_df[col] = melb_df[col].astype('category')
display(melb_df.info())
print(melb_df['Regionname'].cat.categories)
display(melb_df['Regionname'].cat.codes)
melb_df['Type'] = melb_df['Type'].cat.rename_categories({
    'u': 'unit',
    't': 'townhouse',
    'h': 'house'
})
display(melb_df['Type'])
melb_df['Type'] = melb_df['Type'].cat.add_categories('flat')
new_houses_types = pd.Series(['unit', 'house', 'flat', 'flat', 'house'])
new_houses_types = new_houses_types.astype(melb_df['Type'].dtype)
display(new_houses_types)
display(melb_df.info())
popular_suburb = melb_df['Suburb'].value_counts().nlargest(119).index
print(popular_suburb)
melb_df['Suburb'] = melb_df['Suburb'].apply(lambda x: x if x in popular_suburb else 'other')
melb_df['Suburb'] = melb_df['Suburb'].astype('category')
display(melb_df['Suburb'])
display(melb_df.info())