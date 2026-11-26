python pandas
-- StrataScratch
-- LinkedIn
-- ID 10304
-- Risky Projects
-- Medium

import pandas as pd
import numpy as np

employee = pd.merge(linkedin_emp_projects, linkedin_employees, left_on='emp_id', right_on='id')
salary_per_project = employee.groupby('project_id')['salary'].sum()
linkedin_projects['days'] = (pd.to_datetime(linkedin_projects['end_date']) - pd.to_datetime(linkedin_projects['start_date'])).dt.days
linkedin_projects['prorated_cost'] = np.ceil(linkedin_projects['id'].map(salary_per_project) * linkedin_projects['days'] / 365)
overbudget = linkedin_projects[linkedin_projects['prorated_cost'] > linkedin_projects['budget']]
overbudget[['title', 'budget', 'prorated_cost']]
