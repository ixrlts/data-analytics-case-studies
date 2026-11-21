python pandas
-- StrataScratch
-- LinkedIn
-- ID 10077
-- Income By Title and Gender
-- Medium

bonus = sf_bonus.groupby('worker_ref_id')['bonus'].sum().reset_index(name='total_bonus')
merged = pd.merge(sf_employee, bonus, left_on='id', right_on='worker_ref_id', how='right')
merged['total_comp'] = merged['salary'] + merged['total_bonus']
merged.groupby(['employee_title', 'sex'])['total_comp'].mean().reset_index()
