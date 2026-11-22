python pandas
-- StrataScratch
-- Facebook/Meta
-- ID 10352
-- Users By Average Session Time
-- Medium

facebook_web_log['day'] = pd.to_datetime(facebook_web_log['timestamp']).dt.normalize()
facebook_web_log['load'] = facebook_web_log['timestamp'].where(facebook_web_log['action'] == 'page_load')
facebook_web_log['exit'] = facebook_web_log['timestamp'].where(facebook_web_log['action'] == 'page_exit')
daily = facebook_web_log.groupby(['user_id', 'day']).agg(
    load_time=('load', 'max'),
    exit_time=('exit', 'min')
).reset_index()
daily = daily[daily['load_time'] < daily['exit_time']]
daily['session'] = daily['exit_time'] - daily['load_time']
daily.groupby('user_id')['session'].mean().reset_index(name='avg_session_duration')
