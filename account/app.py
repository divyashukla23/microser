from flask import Flask, jsonify
app = Flask(__name__)

USERS = [{"id":1,"name":"Alice"},{"id":2,"name":"Bob"}]

@app.route("/health")
def health():
    return "ok", 200

@app.route("/api/v1/users")
def users():
    return jsonify(USERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
