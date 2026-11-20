python pandas
-- StrataScratch
-- Airbnb
-- ID 10156
-- Number Of Units Per Nationality
-- Medium

merged = pd.merge(airbnb_hosts, airbnb_units, on='host_id')
(merged[(merged['unit_type'] == 'Apartment') & (merged['age'] < 30)]
.groupby('nationality')['unit_id'].nunique().reset_index(name='apartment_count')
.sort_values('apartment_count', ascending=False))
