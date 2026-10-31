import os
import socket

import redis
from flask import Flask, jsonify

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True,
)


@app.route("/")
def index():
    visits = redis_client.incr("visits")
    return jsonify(
        message="Hello from the DevOps Lab!",
        hostname=socket.gethostname(),
        visits=visits,
    )


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
