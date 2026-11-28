python pandas
-- StrataScratch
-- Google, Amazon
-- ID 10090
-- Find the percentage of shippable orders
-- Medium

merged = pd.merge(orders, customers, left_on='cust_id', right_on='id', how='left')
pct = merged['address'].notna().mean() * 100
pd.DataFrame({'shippable_orders_pct': [pct]})
