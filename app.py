from flask import Flask
# import this from views.py
from views import views


app = Flask(__name__)
app.register_blueprint(views, url_prefix = "/")

if __name__ == '__main__':
    # default port is 5000
    app.run(debug=True, port=8000)




