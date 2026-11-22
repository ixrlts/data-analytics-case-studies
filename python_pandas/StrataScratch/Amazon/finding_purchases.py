python pandas
-- StrataScratch
-- Amazon
-- 10553
-- Finding Purchases
-- Medium

amazon_transactions['created_at'] = pd.to_datetime(amazon_transactions['created_at'])
merged = pd.merge(amazon_transactions, amazon_transactions, on='user_id')
returning = merged[(merged['created_at_y'] - merged['created_at_x']).dt.days.between(1, 7)]
returning[['user_id']].drop_duplicates().sort_values('user_id').reset_index(drop=True).reset_index()
