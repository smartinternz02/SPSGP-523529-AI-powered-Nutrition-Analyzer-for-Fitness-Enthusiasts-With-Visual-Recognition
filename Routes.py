from flask import Flask

app = Flask(__name__)

@app.route('/Home')
def demo():
    return "Home Page"

@app.route('/Page2')
def demo1():
    return "Page 2"

if __name__ == "__main__":
    app.run()