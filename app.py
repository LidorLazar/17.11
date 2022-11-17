from flask import Flask


app = Flask(__name__)


studants = [{"name":"lidor", "age":27}]


@app.route("/")
def home():
    return studants



if __name__ == '__main__':
    app.run()