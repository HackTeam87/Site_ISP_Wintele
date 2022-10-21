import sqlite3
from flask import Flask, render_template, url_for, request, redirect
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
     shop = conn.execute('SELECT * FROM shop').fetchall()
     conn.close()
     return render_template('index.html', shop=shop, posts=posts)

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

@app.route("/shop")
def shop():
     shop = 'Магазин'
     return render_template('layouts/shop.html', shop=shop)       


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


@app.route("/get_contact",methods = ['POST'])
def get_contact():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    options = request.form.get('options')
    message = request.form.get('message')

    print(name)
    print(phone)
    print(email)
    print(options)
    print(message)

#     if request.method == 'POST':
#         file = request.files['image']
#         if file and allowed_file(file.filename):
#             # filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], file))

#             p = Post(title=title,tag_id=tag,body=body,file=img)
#             db.session.add(p)
#             db.session.commit()
#         else:
#             p = Post(title=title,tag_id=tag,body=body)
#             db.session.add(p)
#             db.session.commit()


    return redirect('/contact')




if __name__ == "__main__":
    app.run(debug="True", host="0.0.0.0")
