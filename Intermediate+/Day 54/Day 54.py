from flask import Flask

app = Flask(__name__)


@app.route('/')
def helloWorld():
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)

# Learned about basic Flask + Decorator Functions
