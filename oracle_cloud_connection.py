import cx_Oracle

# Oracle DB Connection
def connect_to_oracle_cloud():
    connection = cx_Oracle.connect(user='username', password='password', dsn='your_dsn')
    cursor = connection.cursor()
    return connection, cursor
