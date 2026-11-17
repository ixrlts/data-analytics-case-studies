python pandas
-- StrataScratch
-- Walmart, Best Buy, Dropbox
-- ID 9894
-- Employee and Manager Salaries
-- Medium

merged = pd.merge(employee, employee, left_on='manager_id', right_on='id', suffixes=('_emp', '_mgr'))
final = merged[merged['salary_emp'] > merged['salary_mgr']]
final[['first_name_emp', 'salary_emp']]
