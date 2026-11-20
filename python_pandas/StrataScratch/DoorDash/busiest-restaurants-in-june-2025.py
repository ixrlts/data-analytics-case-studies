python pandas
-- StrataScratch
-- DoorDash
-- ID 10789
-- Busiest Restaurants in June 2025
-- Medium

merged = pd.merge(fooddelivery_orders, fooddelivery_restaurants, on='restaurant_id')
june_delivered = merged[(merged['status'] == 'delivered') & (pd.to_datetime(merged['placed_at']).dt.month == 6)].groupby(['restaurant_id', 'name']).size().reset_index(name='delivered_orders').nlargest(5, 'delivered_orders', keep='all')
