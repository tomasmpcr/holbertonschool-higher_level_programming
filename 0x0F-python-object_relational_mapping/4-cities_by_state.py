#!/usr/bin/python3
""" asdadshfuhdsafh dsfhds """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", user=argv[1],
                           passwd=argv[2], db=argv[3])
    query = conn.cursor()
    sql = "SELECT c.id, c.name, s.name FROM cities c INNER JOIN"
    sql += " states s ON c.state_id = s.id ORDER BY c.id"
    query.execute(sql)
    resultado = query.fetchall()
    for fila in resultado:
        print(fila)
    conn.close()
