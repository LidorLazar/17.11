from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app(CORS)

studants = [{"name":"lidor", "age":27}]


@app.route('/')
def home():
    print(studants)
    return studants



if __name__ == '__main__':
    app.run()