import os


from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
from werkzeug.security import check_password_hash, generate_password_hash

basedir = os.path.abspath(os.path.dirname(__file__))

# Configure application
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem" 
Session(app)

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'posts.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create class for posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(15), nullable=False)
    title = db.Column(db.String(140))
    tags = db.Column(db.String(140), nullable=False)
    pic_path = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Post {self.id}>'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index")
def backcountry():
    return redirect("/")

@app.route("/trailer_tips")
def trailer():
    return render_template("trailer_tips.html")

@app.route("/cooking")
def cooking():
    return render_template("cooking.html")

@app.route("/climbing")
def climbing():
    climbing_posts = Post.query.filter_by(category='Climbing').all()
    return render_template("climbing.html", posts=climbing_posts)

@app.route('/<int:post_id>/')
def climb_post(post_id):
    climbing_post = Post.query.get_or_404(post_id)
    return render_template('climbing-post.html', post=climbing_post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post", methods=('GET', 'Post'))
def post():
    categories = ["Climbing", "Trailer", "Cooking"]
    if request.method == 'POST':
        category = request.form['category']
        title = request.form['title']
        tags = request.form['tags']
        pic_path = request.form['pic']
        content = request.form['content']
        post = Post(category=category, 
                    title=title, 
                    tags=tags,
                    pic_path=pic_path,
                    content=content)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template("post.html", categories=categories)

@app.route("/login-register", methods=["GET", "POST"])
# make sure you render a different page if register is selected
# if log in is accepted, then redirect with welcome, username where login/register used to be
def login_register():
    # Forget any user_id
    session.clear()

    #Make sure username is not blank


    #Make sure username is not blank


    return render_template("login-register.html")


@app.route("/register")
def register():
    return render_template("register.html")