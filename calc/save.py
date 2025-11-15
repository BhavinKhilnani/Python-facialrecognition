def save_history(equation):
    import mysql.connector as con
    import datetime as dt
    result = eval(equation)
    timenow = dt.datetime.now()
    x = con.connect(user='root', password='bhavinishere123@@', host='localhost')
    cur = x.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS calc")
    cur.execute("USE calc")
    cur.execute("CREATE TABLE IF NOT EXISTS history (equation VARCHAR(255), result FLOAT, timestamp VARCHAR(255))")
    cur.execute("INSERT INTO history (equation, result, timestamp) VALUES ('{}', '{}','{}')".format(equation, result, timenow))
    x.commit()
def view_history():
    import mysql.connector as con
    x = con.connect(user='root', password='bhavinishere123@@', host='localhost')
    cur = x.cursor()
    cur.execute("USE calc")
    cur.execute("SELECT * FROM history")
    data = cur.fetchall()
    for row in data:
        print(row[0], "        ", row[1], "        ", row[2])
    x.commit()