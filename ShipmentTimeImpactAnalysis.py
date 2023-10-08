# Sample data
visitors_before = 10000  # Number of visitors before the change
orders_before = 500     # Number of orders before the change

visitors_after = 12000  # Number of visitors after the change
orders_after = 700     # Number of orders after the change

# Calculate conversion rates before and after
conversion_rate_before = (orders_before / visitors_before) * 100
conversion_rate_after = (orders_after / visitors_after) * 100

# Calculate customer retention rate
customers_before = 450   # Number of customers who made repeat purchases before
customers_after = 650    # Number of customers who made repeat purchases after

retention_rate_before = (customers_before / orders_before) * 100
retention_rate_after = (customers_after / orders_after) * 100

# Print results
print(f"Conversion Rate Before: {conversion_rate_before:.2f}%")
print(f"Conversion Rate After: {conversion_rate_after:.2f}%")
print(f"Retention Rate Before: {retention_rate_before:.2f}%")
print(f"Retention Rate After: {retention_rate_after:.2f}%")
