from flask import Flask, jsonify
from core.master import Blockchain

app = Flask(__name__)

# Create blockchain instance
blockchain = Blockchain()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/v1/get_block_height', methods=['GET'])
def get_block_height():
    return jsonify(blockchain.get_latest_block().height)


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=80)
