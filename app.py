from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "¡DZAHUI, the grey cat!"

if __name__ == "__main__":
    app.run(debug=True)

