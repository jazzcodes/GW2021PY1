from flask import *
from Session26 import DB
import hashlib

app = Flask(__name__)
my_db = DB()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def you_can_give_any_name():
    return render_template("login.html")


@app.route("/courses")
def courses():
    return render_template("courses.html")


@app.route("/register-and-save", methods=["POST"])
def register_user_and_save_in_db():

    user = {
        "name": request.form['txtName'],
        "email": request.form['email'],
        "password": request.form['password']
    }

    # Hashing the Password
    user['password'] = hashlib.sha256(user['password'].encode()).hexdigest()

    print(user)

    my_db.insert_operation(collection="users", document=user)

    return render_template("success.html")

@app.route("/users")
def fetch_all_users():
    users = my_db.fetch_documents_in_collection(collection_name="users")
    print("users:", users)
    print("type(users):", type(users))
    return render_template("users.html", result=users)

def main():
    app.run()


if __name__ == '__main__':
    main()
