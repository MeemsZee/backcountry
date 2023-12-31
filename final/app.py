import os


from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import mistune

from sqlalchemy.sql import func, select
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
        'sqlite:///' + os.path.join(basedir, 'website.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create class for posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(15), nullable=False)
    title = db.Column(db.String(140), nullable=False)
    tags = db.Column(db.String(140), nullable=False)
    pic_path = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Post {self.id}>'

# Create class for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<User {self.id}>'
    
categories = ["Climbing", "Trailer", "Cooking"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index")
def backcountry():
    return redirect("/")

@app.route("/trailer_tips")
def trailer():
    trailer_posts = Post.query.filter_by(category='Trailer').all()
    return render_template("trailer_tips.html", posts=trailer_posts)

@app.route("/cooking")
def cooking():
    cooking_posts = Post.query.filter_by(category='Cooking').all()
    return render_template("cooking.html", posts=cooking_posts)

@app.route("/climbing")
def climbing():
    climbing_posts = Post.query.filter_by(category='Climbing').all()
    return render_template("climbing.html", posts=climbing_posts)

@app.route("/post_<int:post_id>/")
def all_post(post_id):
    id = Post.query.get_or_404(post_id)
    md_to_html = mistune.html(id.content)
    return render_template('post-page.html', post=id, html_content=md_to_html)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/garage", methods=('GET', 'POST'))
def post():

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

    return render_template("garage.html", categories=categories)

@app.route("/post_<int:post_id>/edit/", methods=["GET", "POST"])
def edit(post_id):
    post = Post.query.get_or_404(post_id)

    if request.method == 'POST':
        category = request.form['category']
        title = request.form['title']
        tags = request.form['tags']
        pic_path = request.form['pic']
        content = request.form['content']

        post.category=category
        post.title=title
        post.tags=tags
        post.pic_path=pic_path
        post.content=content

        db.session.add(post)
        db.session.commit()
        return redirect(url_for('/post_id'))
    else:
        return render_template("edit.html", post=post, categories=categories)

@app.route("/post_<int:post_id>/delete/")
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect("editable.html")

@app.route("/editable")
def editable():
    posts = Post.query.all()
    return render_template("editable.html", posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()
    if request.method == "POST":
        # Get username
        username = request.form.get("username")

        # Get Password
        password = request.form.get("password")

        # Make sure user and password are correct
        #if username == select(User).where(User.username == username) and password == select(User).where:
        user = User.query.filter_by(username=username).first()
        if username == 'admin-mimi' and check_password_hash(user.password, password):
            session['username'] = user.username
  
        return redirect("/garage")
        
    
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username".lower().strip()]
        password = generate_password_hash(request.form["password".strip()])
        password_confirm = request.form.get("confirmation").strip()
        users_query = User.query.get(username)

        if len(username) == 0 or " " in username  or len(users_query) != 0: 
            return "Invalid username or username unavailable"
        if len(password) == 0: 
            return "Password Required"
        if len(password_confirm) == 0: 
            return "Please re-confirm password"
        if password != password_confirm:
            return "Passwords must match"
        
        user = User(username=username,
                    password=password)
        
        db.session.add(user)
        db.session.commit()

        return redirect("/garage")
    return render_template("register.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")