python pandas
-- StrataScratch
-- Microsoft
-- ID 10299
-- Finding Updated Records
-- Easy

ms_employee_salary.sort_values('salary', ascending=False).drop_duplicates(subset='id')[['id', 'first_name', 'last_name', 'salary', 'department_id']].sort_values('id')
