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
        rows = [(23, 'Bob'),
                (20, 'Tina'),
                (44, 'Jim')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                        rows)
        connection.commit()
        for row in cursor:
            print(row)
finally:
    # Close the connection, regardless of whether the above was sucessfull
    connection.close()