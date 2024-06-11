from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola, món!"

def pex6():
    print("S'està executant el servidor web!")
    app.run()

if __name__ == "__main__":
    pex6()