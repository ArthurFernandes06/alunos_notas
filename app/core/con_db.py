import pymysql
import os
class ConnectionDB:
    def __enter__(self):
        self.connection = pymysql.connect(
            host= os.getenv("MYSQL_HOST"),
            port= int(os.getenv("MYSQL_PORT", 3306)),
            user= os.getenv("MYSQL_USER"),
            password= os.getenv("MYSQL_PASSWORD"),
            database= os.getenv("MYSQL_DATABASE"),
            charset="utf8mb4"
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.connection.rollback()
        else:
            self.connection.commit()

        self.cursor.close()
        self.connection.close()