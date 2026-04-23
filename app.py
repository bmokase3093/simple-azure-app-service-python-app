from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Azure App Service!Stage then Promote to Production"

if __name__ == "__main__":
    app.run()