import psycopg2

from api_tests.params import Par


class DBConnection(object):
    def __init__(self):
        self.session = psycopg2.connect(dbname="easypay_db", user="postgres",
                                        password="postgres", host="localhost")
        self.cursor = None

    def __enter__(self):
        self.cursor = self.session.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def check_price(self):
        self.cursor.execute("SELECT count(*) FROM prices "
                            "WHERE price = %s AND active = TRUE;" % Par.new_price)
        return self.cursor.fetchone()[0]

    def check_delete_inspector(self):
        self.cursor.execute("SELECT count(*) FROM utilities_users "
                            "WHERE user_id = %s;" % Par.inspector_id)
        return self.cursor.fetchone()[0]
