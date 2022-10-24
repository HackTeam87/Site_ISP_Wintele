import os
import sqlite3
import requests
import telebot
from flask import Flask, render_template, url_for, request, redirect, flash
from config import Configuration
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from flask_simple_captcha import CAPTCHA


app = Flask(__name__)
app.config.from_object(Configuration)

CAPTCHA = CAPTCHA(config=app.config['CAPTCHA_CONFIG'])
app = CAPTCHA.init_app(app)


bot_token = os.getenv('BOT_TOKEN', default=None)
bot = telebot.TeleBot(bot_token)
chat_id = os.getenv('CHAT_ID', default=None)



def get_db_connection():
    conn = sqlite3.connect('wintele.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
     ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
     ip_title = ' Ваш IP: ' + ip

     conn = get_db_connection()
     posts = conn.execute('SELECT * FROM posts LIMIT 2').fetchall()
     shop = conn.execute('SELECT * FROM shop').fetchall()
     conn.close()
     return render_template('index.html', ip=ip, ip_title=ip_title, shop=shop, posts=posts)

@app.route("/about-us")
def about_us():
     about_us = 'Про нас'
     return render_template('pages/about-us.html' , about_us=about_us) 

@app.route("/all-price")
def all_price():
     all_price = 'Всі тарифи'
     return render_template('pages/all-price.html' , all_price=all_price)              

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


@app.route("/contact", methods=['GET','POST'])
def contact():
     contact = 'Контакти'

     if request.method == 'GET':
        captcha = CAPTCHA.create()
        return render_template('pages/contact.html', contact=contact, captcha=captcha)
    


@app.route("/get_contact",methods = ['POST'])
def get_contact():       
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        options = request.form.get('options')
        c_hash = request.form.get('captcha-hash')
        c_text = request.form.get('captcha-text')

        m = f''' 
            Заявка з сайту Wintele.com.ua\n
            \n ФИО: {name}  Причина: {options}
            \n Телефон: {phone}  Почта: {email}
          ''' 

        if CAPTCHA.verify(c_text, c_hash) and len(name):
            flash('Дякую! Ми зателефонуємо Вам найближчим часом.', 'alert-primary')
            bot.send_message(chat_id, m)
            return redirect(url_for('contact'))
        else:
            flash('Введіть captcha', 'alert-danger')
            return redirect(url_for('contact')) 


@app.route("/test")
def test():
     return render_template('pages/prices/price1.html' )     

@app.route("/test2")
def test2():
     return render_template('pages/prices/test2.html' )              


if __name__ == "__main__":
    app.run(debug="True", host="0.0.0.0")
