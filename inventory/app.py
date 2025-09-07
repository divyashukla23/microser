from flask import Flask, jsonify
app = Flask(__name__)

PRODUCTS = [{"id":1,"name":"T-shirt","stock":5},{"id":2,"name":"Mug","stock":12}]

@app.route("/health")
def health():
    return "ok", 200

@app.route("/api/v1/products")
def products():
    return jsonify(PRODUCTS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
