from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Mock data for demonstration
risk_data = [
    {"id": 1, "name": "Risk 1", "impact": "High", "probability": "High"},
    {"id": 2, "name": "Risk 2", "impact": "Low", "probability": "Medium"},
    {"id": 3, "name": "Risk 3", "impact": "Medium", "probability": "Low"},
]

@app.route("/")
def index():
    return render_template("index.html", risks=risk_data)

if __name__ == "__main__":
    app.run(debug=True)
