from connection import DBConnect
from create import Create

class Database:
    def __init__(self):
        conn = DBConnect()
        c = Create(conn)
        c.drop_db()
        c.create_db()
        c.create_tables()
        c.use_db()
        c.populate_tables()
        