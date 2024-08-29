from flask import Flask
from routes import quiz_blueprint
from models import db

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

app.register_blueprint(quiz_blueprint)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')

