import os
from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total HTTP requests'
)

MESSAGE = os.getenv(
    'APP_MESSAGE',
    'RabTech Task 6 - Cloud Capstone is running!'
)


@app.before_request
def count_request():
    REQUEST_COUNT.inc()


@app.route('/')
def home():
    return MESSAGE


@app.route('/health')
def health():
    return jsonify(status='healthy'), 200


@app.route('/metrics')
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
