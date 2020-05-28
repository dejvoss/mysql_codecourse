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
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the
        # table already exists
        for row in cursor:
            print(row)
finally:
    # Close the connection, regardless of whether the above was sucessfull
    connection.close()