#!/usr/bin/python3
""" Ej 0 """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host='localhost',
                                 user=argv[1],
                                 passwd=argv[2],
                                 db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

    for row in cur.fetchall():
        print(row)

    conn.close()
