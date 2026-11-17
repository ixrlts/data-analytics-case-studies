python pandas
-- StrataScratch
-- Twitter, Asana
-- ID 9897
-- Highest Salary In Department
-- Medium

grouped = employee[employee['salary'] == employee.groupby('department')['salary'].transform('max')]
grouped[['department', 'first_name', 'salary']]
