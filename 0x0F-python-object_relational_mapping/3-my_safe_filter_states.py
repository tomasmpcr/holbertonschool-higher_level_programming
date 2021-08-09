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

    param = argv[4].split(";")[0]

    sql = "SELECT * FROM states "
    sql += "WHERE states.name = '{}' ORDER BY states.id ASC;".format(param)
    cur.execute(sql)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    conn.close()
