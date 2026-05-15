from flask import Flask

from config import Config

from extensions import ( db,bcrypt, login_manager,mail)

# ================= CREATE APP =================

app = Flask(__name__)

app.config.from_object(Config)

# ================= INITIALIZE EXTENSIONS =================

db.init_app(app)

bcrypt.init_app(app)

login_manager.init_app(app)

mail.init_app(app)

# ================= LOGIN MANAGER =================

login_manager.login_view = 'auth.login'

# ================= IMPORT MODELS =================

from models.user import User
from models.post import Post
from models.comment import Comment
from models.like import Like

# ================= USER LOADER =================

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))

# ================= REGISTER BLUEPRINTS =================

from routes.auth import auth
from routes.main import main
from routes.post_routes import posts
from routes.admin import admin

app.register_blueprint(auth)

app.register_blueprint(main)

app.register_blueprint(posts)

app.register_blueprint(admin)

# ================= CREATE TABLES =================

with app.app_context():

    db.create_all()

# ================= RUN APP =================

if __name__ == '__main__':

    app.run(debug=True)