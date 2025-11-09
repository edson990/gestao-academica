from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Gestão Acadêmica Simplificada</h1><p>Ambiente inicial configurado com Docker Compose ✅</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
