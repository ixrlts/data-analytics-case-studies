python pandas
-- StrataScratch
-- Yelp
-- ID 10049
-- Reviews of Categories
-- Medium

df = yelp_business.copy()
df['category'] = df['categories'].str.split(';')
exploded = df.explode('category')
exploded.groupby('category')['review_count'].sum().reset_index(name='total_reviews').sort_values('total_reviews', ascending=False)
