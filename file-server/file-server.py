from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/assests/<path:path>')
def send_report(path):
    return send_from_directory('assests', path)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=25503)