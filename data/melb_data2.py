import pandas as pd
from IPython.display import display
melb_df = pd.read_csv('data/melb_data.csv', sep=',')
display(melb_df)
print(melb_df['Address'].nunique())
print(melb_df['Address'].loc[177])
def get_street_type(address):
    exclude_list = ['N', 'S', 'W', 'E']
    address_list = address.split(' ')
    street_type = address_list[-1]
    if street_type in exclude_list:
        street_type = address_list[-2]
    return street_type
street_types = melb_df['Address'].apply(get_street_type)
display(street_types)    
print(street_types.nunique())
display(street_types.value_counts())
popular_stypes = street_types.value_counts().nlargest(10).index
print(popular_stypes)
melb_df['StreetType'] = street_types.apply(lambda x: x if x in popular_stypes else 'other') 
display(melb_df['StreetType'])
print(melb_df['StreetType'].nunique())
melb_df = melb_df.drop('Address', axis = 1)
        
        