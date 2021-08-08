#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    miConexion = MySQLdb.connect(host='localhost',
                                 user=argv[1],
                                 passwd=argv[2],
                                 db=argv[3])

    cur = miConexion.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    for row in cur.fetchall():
        print(row)

    miConexion.close()
