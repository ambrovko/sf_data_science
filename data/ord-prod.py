import pandas as pd
from IPython.display import display
ord_df = pd.read_csv('data/orders.csv', sep=';')
prod_df = pd.read_csv('data/products.csv', sep =';')
orders_products = ord_df.merge(
    prod_df,
    left_on = 'ID товара',
    right_on = 'Product_ID',
    how = 'left',
)
display(orders_products.tail(1)['Order ID'])
display(orders_products[orders_products['Отменен'] == 'Да']['Name'])
orders_products['Profit'] = orders_products['Количество'] * orders_products['Price']
mask = orders_products['Оплачен'] == 'Да'
max_profit = orders_products[mask].groupby(by = 'ID Покупателя')['Profit'].sum().sort_values(ascending = False)
display(max_profit)