from model.database import *


def getCustomers(self):
    query ="SELECT sploks.customers.*, sploks.npas.npa, sploks.npas.town FROM sploks.customers LEFT JOIN sploks.npas ON sploks.customers.npa_id = sploks.npas.id"
    connection = connectToDatabase(self) # Opens a connection with the database
    customers = executeQuery(self, connection, query)

    return customers

def getCustomerById(self, id):
    query =f"SELECT sploks.customers.*, sploks.npas.npa FROM sploks.customers LEFT JOIN sploks.npas ON sploks.customers.npa_id = sploks.npas.id  WHERE sploks.customers.id = {id}"
    connection = connectToDatabase(self) # Opens a connection with the database
    customer = executeQuery(self, connection, query)

    return customer

def updateCustomerById(self, id, values):
    query =f"SELECT sploks.npas.id FROM npas WHERE npa = {values['npa']} limit 1 into @npa_id; UPDATE sploks.customers SET customers.lastname = '{values['lastName']}', customers.firstname = '{values['firstName']}', customers.address = '{values['address']}', customers.phone = '{values['phone']}', customers.email = '{values['email']}', customers.mobile = '{values['mobile']}', customers.npa_id = @npa_id WHERE customers.id = '{id}'"
    connection = connectToDatabase(self) # Opens a connection with the database
    output = executeQuery(self, connection, query)
