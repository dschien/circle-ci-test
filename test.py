import unittest

import psycopg2


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.conn = psycopg2.connect("host=db dbname=test user=postgres password=secret")

    def test_db(self):
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS  test (id serial PRIMARY KEY, num integer, data varchar);")
        cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

        cur.execute("SELECT * FROM test;")
        res = cur.fetchone()
        self.assertEqual(res[1], 100)
        self.conn.commit()
        cur.close()
        self.conn.close()


if __name__ == '__main__':
    unittest.main()
