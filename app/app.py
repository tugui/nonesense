from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql:///db.mysql"
# Enter a secret key
app.config["SECRET_KEY"] = "helloworld"
# Initialize flask-sqlalchemy extension

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()