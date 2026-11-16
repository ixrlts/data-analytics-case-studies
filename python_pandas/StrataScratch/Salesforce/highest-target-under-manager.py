python pandas
-- StrataScratch
-- Salesforce
-- ID 9905
-- Highest Target Under Manager
-- Medium

team = salesforce_employees[salesforce_employees['manager_id'] == 13]
top = team[team['target'] == team['target'].max()]
top[['first_name', 'target']]
