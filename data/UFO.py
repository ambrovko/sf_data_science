import pandas as pd
from IPython.display import display
UFO_df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')
UFO_df['Time'] = pd.to_datetime(UFO_df['Time'], dayfirst = True)
UFO_df['Year'] = UFO_df['Time'].dt.year
years_ufo = UFO_df['Time'].dt.year
print(years_ufo.mode()[0])
UFO_df['Date'] = UFO_df['Time'].dt.date
display(UFO_df)
print(UFO_df[UFO_df['State'] == 'NV']['Date'].diff().dt.days.mean())
