from model.database import *


def getCustomers(self):
    query ="SELECT * FROM sploks.customers"

    connection = connectToDatabase(self) # Opens a connection with the database
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall() # Fetch results

    print(results)

    connection.close() # Closes connection

