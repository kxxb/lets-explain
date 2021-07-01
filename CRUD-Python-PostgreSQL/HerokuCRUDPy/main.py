import psycopg2
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def dbConn():
    conn = psycopg2.connect(dbname='df1bj62idpm5dn', user='gyobmmfxaphllq',
                            password='a9f48d10205c2b62a3b8ad3f269de7a557e80c00bee78ac90cb7179d3afaac16',
                            host='ec2-52-31-233-101.eu-west-1.compute.amazonaws.com')
    return conn

def getData():
    sql ='select * from users'
    conn = dbConn()
    c = conn.cursor()
    c.execute(sql)
    records = c.fetchall()
    for row in records:
        print(row)
    ...
    c.close()

def insertData():
    id = 2
    name = 'Insert user'
    record = (id, name)
    sql = """insert into users (id, name )  values ( %s, %s ); """
    conn = dbConn()
    c = conn.cursor()
    c.execute(sql, record)
    conn.commit()

def updateData():
    id = 2
    name = 'Update user'
    record = (name, id)
    sql = """update users set  name = %s  where id = %s; """
    conn = dbConn()
    c = conn.cursor()
    c.execute(sql, record)
    conn.commit()

def delData():
    id = 2
    record = (id,)
    sql = """delete from users where id = %s """
    conn = dbConn()
    c = conn.cursor()
    c.execute(sql, record)
    conn.commit()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    delData()
    getData()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
