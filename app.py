from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "welcome to travis ci"

def main():
    app.run(port=5000, host="0.0.0.0", debug=False)

if __name__ == '__main__':
    main()