from src.database.connections.mysql.mysql import MySQLDB


def get_mysql_db():
    db = MySQLDB()
    try:
        yield db.session
    finally:
        db.session.close()
