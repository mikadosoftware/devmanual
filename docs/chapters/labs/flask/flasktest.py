from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return str(request.environ)

if __name__ == "__main__":
    app.run()