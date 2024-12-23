import sqlite3

connection=sqlite3.connect("database.db")
cursor=connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INT,
username TEXT,
age INT,
shop TEXT,
block INT
);
''')


def add_user(user_id,username,age):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO Users (id, username, age, block) VALUES(?, ?, ?, ?)',    (user_id,username, age, 0))
    connection.commit()

def get_user(id):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    user_FIND=cursor.execute(f'SELECT * FROM Users WHERE id={id}')
    #print(f'get_user={user_FIND.fetchone()}')
    if user_FIND.fetchone() is None:
        connection.commit()
        print("нет такого")
        # нет еще такого пользователя
        return False
    else:
        connection.commit()
        print("я уже")
        # нашли таких
        return True

def get_all_users():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    user_FIND=cursor.execute(f'SELECT * FROM Users ')
    return user_FIND.fetchall()

def count_stat():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    count_users=cursor.execute("SELECT COUNT(*) FROM Users").fetchone()
    connection.commit()
    return count_users[0]


def add_to_block(input_id):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    print(get_user(input_id))
    if get_user(input_id)==True:
        cursor.execute(f'UPDATE Users SET block =? WHERE id=?', (1,input_id))
        connection.commit()
        return True
    else:
        return False

def remove_block(input_id):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    print(get_user(input_id))
    if get_user(input_id)==True:
        cursor.execute(f'UPDATE Users SET block =? WHERE id=?', (0,input_id))
        connection.commit()
        return True
    else:
        return False



def check_block(user_id):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    users=cursor.execute(f"SELECT block FROM Users WHERE id={user_id}").fetchone()
    connection.commit()
    if users is None:
        return None
    if users[0]==1:
        return users[0]
    else:
        return None




connection.commit()
connection.close()