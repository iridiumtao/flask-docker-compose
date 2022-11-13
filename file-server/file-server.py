from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/assets/<path:path>')
def serve_assets(path):
    return send_from_directory('assets', path)

@app.route('/outputs/<path:path>')
def serve_outputs(path):
    return send_from_directory('outputs', path)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=25503)
