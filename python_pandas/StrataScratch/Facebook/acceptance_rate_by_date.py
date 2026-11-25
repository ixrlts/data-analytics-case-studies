python pandas
-- StrataScratch
-- Facebook/Meta
-- ID 10285
-- Acceptance Rate By Date
-- Medium

df = fb_friend_requests
sent = df[df['action'] == 'sent']
accepted = df[df['action'] == 'accepted']
merged = pd.merge(sent, accepted, on=['user_id_sender', 'user_id_receiver'], how='left', indicator=True)
merged['accepted'] = merged['_merge'] == 'both'
pair = merged.drop_duplicates(subset=['date_x', 'user_id_sender', 'user_id_receiver'])
acc_rate = pair.groupby('date_x')['accepted'].mean().round(2).reset_index()
acc_rate[acc_rate['accepted'] > 0].sort_values('date_x')
