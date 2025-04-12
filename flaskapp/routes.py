import os
import secrets
from flask import render_template, url_for, flash, redirect, request, abort
from flaskapp import app, db, bcrypt
from flaskapp.models import User, Post
from flaskapp.forms import RegistrationForm, LoginForm, PostForm
from flask_login import login_user, current_user, logout_user, login_required


# I don't know why this works or why its needed but it fixes like 30 mins worth of errors with the database...
app.app_context().push()

# First startup check (no tables in db) (Thank you john flamkimmer very nice very epic)
try:
    User.query.first()
except:
    db.create_all()
    print("Database Init!")

# No users check
if User.query.first() is None:
    hashed_password = bcrypt.generate_password_hash("admin").decode('utf-8')
    user = User(username="admin", password=hashed_password)
    db.session.add(user)
    db.session.commit()

# ============================
# ===== Helper Functions =====
# ============================



# ==================
# ===== Routes =====
# ==================

@app.route("/")
@app.route("/home")
def render_index():
    posts = Post.query.order_by(Post.date_posted.desc())
    return render_template('index.html', posts=posts)

@app.route("/about/")
def render_about():
    return render_template('about.html')

@app.route("/blog/<blog_id>")
def render_blog(blog_id="None"):
    post = Post.query.get_or_404(blog_id)
    return render_template('blog.html', title=post.title, post=post)

# ========================
# ===== Admin Routes =====
# ========================

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('render_index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next') # Redirect back to the page a user was originally trying to get to
            return redirect(next_page) if next_page else redirect(url_for('render_index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger mt-4')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('render_index'))

@app.route("/create-blog", methods=['GET', 'POST'])
@login_required
def create_blog():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, authors=form.authors.data, blog_type=form.blog_type.data, description=form.description.data)
        db.session.add(post)
        db.session.commit()
        flash('Post has been created!', 'success mt-4')
        return redirect(url_for('render_index'))
    return render_template('create-blog.html', title='New Blog', form=form, legend='New Blog')

@app.route("/register", methods=['GET', 'POST'])
@login_required
def register():
    if current_user.is_authenticated:
    # if True:
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in.', 'success mt-4')
            return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)
    return redirect(url_for('render_index'))

@app.route("/display_users")
@login_required
def display_users():
    users = User.query.all()
    return render_template('display_users.html', title='CoboBlog Admins', users=users)

@app.route("/display_users/<int:user_id>/delete", methods=['POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    user_posts = Post.query.filter_by(user_id=user_id).all()

    for post in user_posts:
        db.session.delete(post)
    db.session.delete(user)
    db.session.commit()

    flash('User has been deleted!', 'success mt-4')
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', title='Home', posts=posts)

@app.route("/blog/<int:blog_id>/delete", methods=['POST'])
@login_required
def delete_blog(blog_id):
    post = Post.query.get_or_404(blog_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted!', 'success mt-4')
    return redirect(url_for('render_index'))