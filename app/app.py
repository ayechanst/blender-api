from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get_planets", methods=["POST"])
def get_planets():
    data = request.get_json()
    print("Received data: ", data)
    return jsonify({"message": "Planet data received"}), 200

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!", 200

if __name__ == "__main__":
    app.run(debug=True)