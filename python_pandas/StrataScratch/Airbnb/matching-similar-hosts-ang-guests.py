python pandas
-- StrataScratch
-- Airbnb
-- ID 10078
-- Matching Similar Hosts and Guests
-- Medium

merged = pd.merge(airbnb_hosts, airbnb_guests, on=['nationality', 'gender'])
merged[['host_id', 'guest_id']].drop_duplicates()
