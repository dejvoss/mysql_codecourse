import os
import datetime
import pymysql

# Get username from Cloud0 workspace
# (modify this variable if runing on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host = 'localhost',
                            user=username,
                            password='',
                            db='Chinook')


try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
                ("Jim", 56, "1955-05-09 13:23:22"),
                ("Tina", 22, "1998-02-03 12:10:44")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s)", rows)
        connection.commit()
        for row in cursor:
            print(row)
finally:
    # Close the connection, regardless of whether the above was sucessfull
    connection.close()