from model.database import *


def getCustomers(self):
    query ="SELECT * FROM sploks.customers"

    connection = connectToDatabase(self) # Opens a connection with the database
    cursor = connection.cursor()
    cursor.execute(query)
    customers = cursor.fetchall() # Fetch results
    connection.close() # Closes connection

    return customers

