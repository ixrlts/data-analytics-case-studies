python pandas
-- StrataScratch
-- Amazon, Groupon, Salesforce
-- ID 10127
-- Calculate Samantha`s and Lisa`s total sales revenue
-- Easy

sales_performance[sales_performance['salesperson'].isin(['Samantha', 'Lisa'])]['sales_revenue'].sum()
