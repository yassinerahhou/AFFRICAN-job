# AJITKHDEM_V2
import sqlite3

# Connect to the source database
source_conn = sqlite3.connect('sitea.db')
source_cursor = source_conn.cursor()

# Connect to the target database
target_conn = sqlite3.connect('test.db')
target_cursor = target_conn.cursor()

# Fetch data from the source database
source_cursor.execute('SELECT * FROM post')
data = source_cursor.fetchall()

# Insert data into the target database
target_cursor.executemany('INSERT INTO your_table_name VALUES (?, ?, ...)', data)

# Commit the changes and close connections
target_conn.commit()
source_conn.close()
target_conn.close()

import sqlite3

# Connect to the "sitea.db" database
sitea_conn = sqlite3.connect('sitea.db')
sitea_cursor = sitea_conn.cursor()

# Execute the query to get the list of tables in "sitea.db"
sitea_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch and print the results
sitea_tables = sitea_cursor.fetchall()
print("Tables in sitea.db:")
for table in sitea_tables:
    print(table[0])

# Close the connection to "sitea.db"
sitea_conn.close()

# Connect to the "test.db" database
test_conn = sqlite3.connect('test.db')
test_cursor = test_conn.cursor()

# Execute the query to get the list of tables in "test.db"
test_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch and print the results
test_tables = test_cursor.fetchall()
print("\nTables in test.db:")
for table in test_tables:
    print(table[0])

# Close the connection to "test.db"
test_conn.close()
