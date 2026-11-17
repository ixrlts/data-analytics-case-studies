python pandas
-- StrataScratch
-- Lyft
-- ID 10004
-- Find all Lyft rides which happened on rainy days before noon
-- Easy

rainy_day = lyft_rides[lyft_rides['weather'] == 'rainy'][lyft_rides['hour'] < 12]
rainy_day
