python pandas
-- StrataScratch
-- Airbnb
-- ID 10159
-- Ranking Most Active Guests
-- Medium

grouped = airbnb_contacts.groupby('id_guest')['n_messages'].sum().reset_index()
grouped['ranking'] = grouped['n_messages'].rank(method='dense', ascending=False)
grouped[['ranking', 'id_guest', 'n_messages']].sort_values('ranking')
