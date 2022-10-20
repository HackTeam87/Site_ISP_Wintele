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
    


    query1 = ''' INSERT INTO shop (price, title, content) VALUES ('test0','test3', 'test4') '''
    cursor.execute(query_create_shop_table)

    # db.commit()
    

    query2 = ''' SELECT * FROM shop '''
    res = cursor.execute(query2)

for p in res:
    print(p) 

# db.close()   


