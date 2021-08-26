"""
    Light Weight Web App Development
    Flask
    For a detailed exploration -> https://flask.palletsprojects.com/en/2.0.x/
    -> Choose the path -> Django For career in Web Dev
    -> Choose the path -> numpy/pandas/matplotlib/sklearn .... in Data Science

    Use ngrok for exposing web app to public
    https://ngrok.com/docs

    command -> ngrok http 5000
"""

# from flask import Flask
from flask import *
# Flask shall WSGI Server: use https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface

# Create the object of your web app
# app = Flask("MyWebApp")
app = Flask(__name__)

@app.route("/")
def index_page():
    text_response = "Welcome to My Flask Web App"
    return text_response

@app.route("/welcome")
def welcome():
    html_response = """
    <html>
        <title>
            Welcome
        </title>
        <body>
            <center>
                <h3>Welcome to MyApp with Flask WISGI Server</h3>
                You can Register or Login
            </center>
        </body>
    </html>    
    """

    # return html_response
    return render_template("index.html")

def main():
    app.run()

if __name__ == '__main__':
    main()