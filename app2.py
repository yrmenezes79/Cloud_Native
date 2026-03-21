from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Bem-vindo à Cafeteria Docker!</h1><p>O container está servindo seu café com sucesso.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
