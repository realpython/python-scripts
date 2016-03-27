import sys
import csv
import sqlite3

if len(sys.argv) < 3:
    print("Use: {0} DATABASE_NAME TABLE_NAME".format(sys.argv[0]))
    exit()

conn = sqlite3.connect(sys.argv[1])
cur = conn.cursor()
data = cur.execute("SELECT * FROM {0}".format(sys.argv[2]))

with open('output.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(data)

conn.close()
