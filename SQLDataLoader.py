import pyodbc

# Connection setup
server = '.'
database = 'BMT'
driver = 'SQL Server'  # This depends on your installed driver


class SalesSQLRepository:

    def fetchSales(self):
        # Create a connection
        conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database}'
        conn = pyodbc.connect(conn_str)

        # Create a cursor
        cursor = conn.cursor()

        # Execute a query
        query = 'SELECT * FROM SALES'
        cursor.execute(query)

        # Fetch data
        rows = cursor.fetchall()

        # Close cursor and connection
        cursor.close()
        conn.close()

        return rows
