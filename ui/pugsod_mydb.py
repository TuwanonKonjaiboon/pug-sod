import mysql.connector
from mysql.connector import Error

class sql:
    @staticmethod
    def query(query):
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='root',
                                         password='be1234er')

            if connection.is_connected():
                db_Info = connection.get_server_info()
                cursor = connection.cursor()
        
                cursor.execute(query)
                result = cursor.fetchall()

                cursor.close()
                connection.close()

                return result
                
        except Error as e:
            print("Error while connecting to MySQL", e)
