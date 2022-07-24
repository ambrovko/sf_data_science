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
def get_weekend(weekday):
    if weekday == 5 or weekday == 6:
        return 1
    else:
        return 0
melb_df['Weekend'] = melb_df['WeekdaySale'].apply(get_weekend)
display(melb_df['Weekend'])
aver_price = melb_df[melb_df['Weekend'] == 1]['Price'].mean()
print(round(aver_price))