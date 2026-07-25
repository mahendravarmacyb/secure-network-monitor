import sqlite3
import os


class Database:
    def __init__(self, db_path="database/network.db"):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        os.makedirs("database", exist_ok=True)
        self.connection = sqlite3.connect(self.db_path)
        return self.connection

    def initialize(self):
        conn = self.connect()

        with open("database/schema.sql", "r") as file:
            schema = file.read()

        conn.executescript(schema)
        conn.commit()

        print("Database initialized successfully.")

    def close(self):
        if self.connection:
            self.connection.close()
