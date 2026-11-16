python pandas
-- StrataScratch
-- OpenAI/ChatGPT
-- ID 10597
-- Thumbs-Up Rate by Model Version
-- Medium

only_rated = ai_response_feedback[ai_response_feedback['feedback'].isin(['thumbs_up', 'thumbs_down'])]
only_rated['up_id'] = only_rated['response_id'].where(only_rated['feedback'] == 'thumbs_up')
grouped = only_rated.groupby('model_version').agg(
        ups=('up_id', 'nunique'),
        total=('response_id', 'nunique')
).reset_index()
grouped['thumbs_up_pct'] = (100 * grouped['ups'] / grouped['total']).round()
grouped[['model_version', 'thumbs_up_pct']].sort_values('model_version')
