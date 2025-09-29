from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/status")
def api_status():
    return {
        "status": "success",
        "service": "Full-Stack Portfolio Backend",
        "message": "Python/Flask server is running and responding to API calls.",
        "developer": "Edidiong Aaron"
    }

if __name__ == "__main__":
    app.run(debug=True)