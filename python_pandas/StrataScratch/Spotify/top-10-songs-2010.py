python pandas
-- StrataScratch
-- Spotify
-- ID 9650
-- Top 10 Songs 2010
-- Medium

filtered = billboard_top_100_year_end[(billboard_top_100_year_end['year'] == 2010) & (billboard_top_100_year_end['year_rank'] < 11)]
filtered[['year_rank', 'group_name', 'song_name']].drop_duplicates()
