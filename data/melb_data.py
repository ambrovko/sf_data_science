import pandas as pd
from IPython.display import display
melb_df = pd.read_csv('data/melb_data.csv', sep=',')
melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
display(melb_df['Date'])
melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek
display(melb_df['WeekdaySale'])
display(melb_df['WeekdaySale'].value_counts())
weekend_count = melb_df[(melb_df['WeekdaySale'] == 5) | (melb_df['WeekdaySale'] == 6)].shape[0]
print(weekend_count)