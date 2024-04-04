import sqlite3

conn = sqlite3.connect('data.db')

cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Leaderboard (
name TEXT NOT NULL,
score INT)
''')


def add_to_the_database(name, score):
    cur.execute('INSERT INTO Leaderboard (name, score) VALUES (?, ?)', (name, score))
    conn.commit()


def printsql():
    cur.execute('''SELECT * FROM Leaderboard ORDER BY score DESC Limit 10''')
    return cur.fetchall()


def printsql_by_name(name):
    cur.execute('SELECT * FROM Leaderboard WHERE name = ?', (name,))
    return cur.fetchone()


def update_score(name, new_score):
    cur.execute('SELECT score FROM Leaderboard WHERE name = ?', (name,))
    current_score = cur.fetchone()
    if current_score is not None:
        current_score = current_score[0]
        if new_score > current_score:
            cur.execute('UPDATE Leaderboard SET score = ? WHERE name = ?', (new_score, name))
            conn.commit()
            return False


def check_name_in_db(name):
    cur.execute("SELECT EXISTS(SELECT 1 FROM Leaderboard WHERE name=?)", (name,))
    record = cur.fetchone()
    if record[0] == 1:
        return True
    else:
        return False


def sqlupdate(name, score):
    if check_name_in_db(name):
        update_score(name, score)
    else:
        add_to_the_database(name, score)



