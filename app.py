from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    # Simple check: if this code runs, the service is up.
    return jsonify(status="ok"), 200

if __name__ == '__main__':
    # Listen on all interfaces within the container on port 5000
    # Use a different port if desired.
    app.run(host='0.0.0.0', port=5000)