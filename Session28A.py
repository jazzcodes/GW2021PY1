from flask import *
from Session26 import DB

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

    print(user)

    my_db.insert_operation(collection="users", document=user)

    return "THANK YOU FOR REGISTERING WITH US"

def main():
    app.run()


if __name__ == '__main__':
    main()


# https://4ae8-124-253-48-130.ngrok.io
