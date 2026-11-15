python pandas
-- StrataScratch
-- Amazon, Etsy
-- ID 10183
-- Total Cost Of Orders
-- Easy

import pandas as pd
merged = pd.merge(customers, orders, left_on='id', right_on='cust_id', how='inner')
merged.groupby(['cust_id', 'first_name'])['total_order_cost'].sum().reset_index().sort_values('first_name')
