import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

###############################################
    ########### DATABASE SETUP #############
###############################################
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

#################################################
    ############# LOGIN MANAGER #############
################################################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'




##################################################
from puppy_company_blog.core.views import core
from puppy_company_blog.error_pages.handler import error_pages
from puppy_company_blog.users.views import users
from puppy_company_blog.blog_post.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
