from model.database import *


def getCustomers(self):
    query ="SELECT sploks.customers.*, sploks.npas.npa, sploks.npas.town FROM sploks.customers LEFT JOIN sploks.npas ON sploks.customers.id = sploks.npas.id"
    connection = connectToDatabase(self) # Opens a connection with the database
    customers = executeQuery(self, connection, query)

    return customers

def getCustomerById(self, id):
    query =f"SELECT * FROM sploks.customers WHERE sploks.customers.id = {id};"
    connection = connectToDatabase(self) # Opens a connection with the database
    customer = executeQuery(self, connection, query)

    return customer
