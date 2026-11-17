python pandas
-- StrataScratch
-- Yelp
-- ID 10060
-- Top Cool Votes
-- Medium

coolest = yelp_reviews[yelp_reviews['cool'] == yelp_reviews['cool'].max()]
coolest[['business_name', 'review_text']]
