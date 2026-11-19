python pandas
-- StrataScratch
-- Amazon
-- ID 10322
-- Finding User Purchases
-- Medium

amazon_transactions['purchase_date'] = pd.to_datetime(amazon_transactions['created_at']).dt.normalize()
amazon_transactions['first_purchase'] = amazon_transactions.groupby('user_id')['purchase_date'].transform('min')
amazon_transactions['second_purchase'] = (amazon_transactions['purchase_date'] - amazon_transactions['first_purchase']).dt.days
filtered = amazon_transactions[amazon_transactions['second_purchase'].between(1, 7)]
filtered[['user_id']].drop_duplicates()
