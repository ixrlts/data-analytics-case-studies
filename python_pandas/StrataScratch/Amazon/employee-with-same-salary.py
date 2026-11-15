python pandas
-- StrataScratch
-- Amazon
-- ID 9856
-- Employees With the Same Salary
-- Medium

worker[worker['salary'].duplicated(keep=False)][['worker_id', 'first_name', 'salary']].sort_values('salary')
