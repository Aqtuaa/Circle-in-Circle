from flask import Flask, request, jsonify, render_template
from sklearn.datasets import make_circles

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/circles", methods=["POST"])
def circles():
    data = request.get_json()

    n_samples = data.get("n_samples", 300)
    noise = data.get("noise", 0.05)

    x, y = make_circles(n_samples=n_samples, noise=noise)

    return jsonify({
        "X": x.tolist(),
        "y": y.tolist()
    })

if __name__ == "__main__":
    app.run(debug=True)