#!/usr/bin/python3
""" ASDDSFDJNSFIDSHFIDSHFSD """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    argument = argv[4]
    conn = MySQLdb.connect(host="localhost", user=argv[1],
                           passwd=argv[2], db=argv[3])
    query = conn.cursor()
    query.execute("SELECT GROUP_CONCAT(cities.name SEPARATOR\
                     ', ') FROM cities INNER JOIN states ON states.name\
                      = %s WHERE cities.state_id = states.id ORDER\
                       BY cities.id ASC;", (argument,))
    resultado = query.fetchall()
    for fila in resultado:
            p = str(fila).replace(",)", "")
            p = p.replace("(", "")
            p = p.replace("'", "")
            if (p != 'None'):
                print(p)
            else:
                print()
    conn.close()
    