from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello from Flask!"

@app.route('/monitor/info', methods=['GET'])
def monitor_info():
    return jsonify({"state": "Healthy"})

if __name__ == '__main__':
    app.run(debug=True)
