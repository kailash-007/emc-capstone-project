from database import get_db
import flask_bcrypt as bcrypt

def create_user(username, password):
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    db = get_db()
    db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, pw_hash))
    db.commit()

def get_user(username):
    db = get_db()
    return db.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()

def validate_login(username, password):
    user = get_user(username)
    if user is None:
        return False
    return bcrypt.check_password_hash(user["password"], password)

def add_note(user_id, note):
    db = get_db()
    db.execute("INSERT INTO notes (user_id, note) VALUES (?, ?)", (user_id, note))
    db.commit()

def get_notes(user_id):
    db = get_db()
    return db.execute("SELECT * FROM notes WHERE user_id=?", (user_id,)).fetchall()
