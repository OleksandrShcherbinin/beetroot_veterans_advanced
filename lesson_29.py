import sqlite3


with sqlite3.connect('social.db') as conn:
    cursor = conn.cursor()
    user_id = input('Input user id: ')
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    conn.commit()
    result = cursor.fetchall()
    print(result)