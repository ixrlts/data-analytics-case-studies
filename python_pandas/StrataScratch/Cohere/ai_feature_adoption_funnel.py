python pandas
-- StrataScratch
-- Cohere, Anthropic
-- ID 10583
-- AI Feature Adoption Funnel
-- Medium

df = ai_funnel_events 
first_use = df[df['event_type'].isin(['first_use', 'repeat_use'])]['user_id'].nunique()
impression = df[df['event_type'] == 'impression']['user_id'].nunique()
repeat_use = df[df['event_type'] == 'repeat_use']['user_id'].nunique()
pd.DataFrame({
    'funnel_stage': ['first_use', 'impression', 'repeat_use'],
    'users': [first_use, impression, repeat_use]
})
