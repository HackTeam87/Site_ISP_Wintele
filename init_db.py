import sqlite3

with sqlite3.connect('./wintele.db') as db:
    cursor = db.cursor()

    query_create_posts_table = ''' CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    short_content TEXT NOT NULL,
    content TEXT NOT NULL,
    img_link TEXT
        ); '''
    cursor.execute(query_create_posts_table)


    query_create_shop_table = ''' CREATE TABLE IF NOT EXISTS shop (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    price TEXT NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    img_link TEXT
        ); '''
    cursor.execute(query_create_shop_table)   
    
    db.commit()
    
db.close()   


