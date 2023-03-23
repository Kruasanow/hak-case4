import psycopg2
import csv

# Connect to the PostgreSQL database
conn = psycopg2.connect(database="hack_db", user="hackaton", password="vkathebest", host="localhost", port="5432")
cur = conn.cursor()

# Open the CSV file
with open('data-1679604281294.csv', 'r') as f:
    # Create a CSV reader object
    reader = csv.reader(f)

    # Skip the header row
    next(reader)

    # Iterate over each row in the CSV file
    for row in reader:
        # Insert the row into the PostgreSQL database
        cur.execute("INSERT INTO test (column1, column2, column3) VALUES (%s, %s, %s)", str(row))

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()