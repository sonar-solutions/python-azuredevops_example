from mysql.connector import connection
connection.MySQLConnection(host='localhost', user='sonarsource', password='')  # Noncompliant


class MyClass(object):
    def __init__(self):
        self.message = 'Hello'
        return self  # Noncompliant
