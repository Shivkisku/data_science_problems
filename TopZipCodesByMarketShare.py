import sqlite3

# Create a SQLite database (or connect to an existing one)
conn = sqlite3.connect("house_listings.db")
cursor = conn.cursor()

# Create and populate the "house_listings" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS house_listings (
        house_id INTEGER,
        zip_code INTEGER,
        price REAL,
        listing_date DATETIME
    )
''')

cursor.executemany('''
    INSERT INTO house_listings (house_id, zip_code, price, listing_date)
    VALUES (?, ?, ?, ?)
''', [
    (1, 90210, 1500000.0, "2023-01-01 10:00:00"),
    # Add more house listing data here...
])

# Commit changes and close the connection
conn.commit()
conn.close()

# Connect to the database again
conn = sqlite3.connect("house_listings.db")
cursor = conn.cursor()

# Write the SQL query to get the top 5 zip codes by market share
sql_query = '''
    SELECT zip_code, SUM(price) / (SELECT SUM(price) FROM house_listings) AS market_share
    FROM house_listings
    GROUP BY zip_code
    HAVING COUNT(*) >= 10000
    ORDER BY market_share DESC
    LIMIT 5
'''

# Execute the query and retrieve the results
cursor.execute(sql_query)
results = cursor.fetchall()

# Print the top 5 zip codes by market share
print("Top 5 zip codes by market share of house prices:")
for i, (zip_code, market_share) in enumerate(results, start=1):
    print(f"{i}. Zip Code {zip_code}: Market Share = {market_share:.4f}")

# Close the connection
conn.close()
