python pandas
-- StrataScratch
-- ESPN
-- ID 9943
-- Olympics Events List By Age
-- Easy

olympics_athletes_events['age'].agg(['min', 'mean', 'max']).to_frame().T
