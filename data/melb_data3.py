import pandas as pd
from IPython.display import display
melb_df = pd.read_csv('data/melb_data.csv', sep=',')
print(melb_df['SellerG'].nunique())
display(melb_df['SellerG'])
popular_estate = melb_df['SellerG'].value_counts().nlargest(49).index
print(popular_estate)
melb_df['SellerG'] = melb_df['SellerG'].apply(lambda x: x if x in popular_estate else 'other')
a = melb_df[melb_df['SellerG'] == 'Nelson']['Price'].min()
b = melb_df[melb_df['SellerG'] == 'other']['Price'].min()
print(round(a/b, 1))