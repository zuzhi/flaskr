from flaskr import create_app, db

app = create_app()

with app.app_context():
    db.init_db()