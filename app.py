import sqlite3
from flask import Flask, render_template, url_for
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('wintele.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
     conn = get_db_connection()
     posts = conn.execute('SELECT * FROM posts LIMIT 2').fetchall()
     conn.close()
     return render_template('index.html', posts=posts)

@app.route("/about-us")
def about_us():
     about_us = 'Про нас'
     return render_template('pages/about-us.html' , about_us=about_us) 

@app.route("/all-price")
def all_price():
     all_price = 'Всі тарифи'
     return render_template('pages/all-price.html' , all_price=all_price)              

@app.route("/contact")
def contact():
     contact = 'Контакти'
     return render_template('pages/contact.html', contact=contact)   


@app.route("/post-detail/<int:id>", methods = ['GET', 'POST'])
def post_detail(id):
     conn = get_db_connection()
     post = conn.execute('SELECT * FROM posts WHERE id = ?',(id,)).fetchone()
     conn.close()
     post_detail = post['title']
     return render_template('pages/post-detail.html', post_detail=post_detail, post=post)

@app.route("/all-blog-posts")
def all_blog_posts():
     all_blog_posts = 'Всі новини'
     conn = get_db_connection()
     posts = conn.execute('SELECT * FROM posts').fetchall()
     conn.close()
     return render_template('pages/all-blog-posts.html', all_blog_posts=all_blog_posts, posts=posts)           



if __name__ == "__main__":
    app.run(debug="True", host="0.0.0.0")
