def fetch_data_from_cloud(connection, cursor):
    query = "SELECT * FROM bitcoin_data"
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows
