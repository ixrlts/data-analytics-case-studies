python pandas
-- StrataScratch
-- Lyft
-- ID 10005
-- Hour Of Highest Gas Expense
-- Easy

lyft_rides[lyft_rides['gasoline_cost'] == lyft_rides['gasoline_cost'].max()][['hour']]
