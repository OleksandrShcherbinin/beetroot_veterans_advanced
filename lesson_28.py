import sqlite3


def create_connection(path: str) -> sqlite3.Connection:
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('Connected to db', path)
    except sqlite3.Error as e:
        print(f'Error while connecting to db {e}')

    return connection


def execute_query(connection: sqlite3.Connection, query: str) -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print('Query executed', query)
    except sqlite3.Error as e:
        print(f'Error while executing to db {e}')


create_table_users = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT,
    location TEXT    
)
"""

connection = create_connection('social.db')
# execute_query(connection, create_table_users)

create_table_posts = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
"""
# execute_query(connection, create_table_posts)

create_table_comments = """
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (post_id) REFERENCES posts (id)
)
"""

create_table_likes = """
CREATE TABLE IF NOT EXISTS likes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (post_id) REFERENCES posts (id)
)
"""

# execute_query(connection, create_table_comments)
# execute_query(connection, create_table_likes)

create_users = """
INSERT INTO
    users (name, age, gender, location)
VALUES 
    ('Oleksandr', 33, 'male', 'Kyiv'),
    ('Andriy', 27, 'male', 'Lviv'),
    ('Inna', 20, 'female', 'Terniopil'),
    ('Dmytro', 28, 'male', 'Kyiv'),
    ('Anastasia', 21, 'female', 'Odesa')
"""

# execute_query(connection, create_users)

create_posts = """
INSERT INTO
    posts (title, description, user_id)
VALUES 
    ('Щастя', 'Сьогодні я щасливий', 1),
    ('Спекотно', 'Сьогодні дуже спекотно', 2),
    ('Допомога', 'Допоможіть розібратись з SQL', 3),
    ('Гарні новини', 'Я отримав сертифікат від Бітрут', 4),
    ('Прекрасні новини', 'Завтра я іду на співбесіду', 5),
    ('Вечірка', 'Хто іде зі мною на вечірку', 4)
"""

# execute_query(connection, create_posts)

create_comments = """
INSERT INTO
    comments (text, user_id, post_id)
VALUES 
    ('Радий за тебе', 5, 1),
    ('Що саме не зрозуміло', 1, 3),
    ('Вітаю', 4, 5),
    ('Дуже радий тебе', 2, 4),
    ('Давай зізвонимося, я допоможу', 5, 3),
    ('Мої вітання', 3, 4)
"""

# execute_query(connection, create_comments)

create_likes = """
INSERT INTO
    likes (user_id, post_id)
VALUES 
    (1, 6),
    (2, 3),
    (1, 5),
    (5, 4),
    (2, 4),
    (4, 2),
    (3, 6)
"""
# execute_query(connection, create_likes)


def select_query(connection: sqlite3.Connection, query: str) -> list | None:
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f'Error during select {e}')


select_users = 'SELECT * FROM users'

users = select_query(connection, select_users)

for user in users:
    print(user)


select_users_posts = """
SELECT
    users.name,
    posts.title,
    posts.description
FROM posts
INNER JOIN users ON users.id = posts.user_id
"""

posts = select_query(connection, select_users_posts)

print('*' * 100)
for post in posts:
    print(post)


select_post_comments_users = """
SELECT 
    posts.description as post,
    text as comment,
    name
FROM posts
INNER JOIN comments ON posts.id = comments.post_id
INNER JOIN users ON users.id = comments.user_id  
"""

posts = select_query(connection, select_post_comments_users)

print('*' * 100)
for post in posts:
    print(post)


select_posts_likes = """
SELECT
    description as post,
    COUNT(likes.id) as likes
FROM likes, posts
WHERE posts.id = likes.post_id
GROUP BY likes.post_id
"""

posts = select_query(connection, select_posts_likes)

print('*' * 100)
for post in posts:
    print(post)