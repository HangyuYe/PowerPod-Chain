from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/api/v1/get_block_height', methods=['GET'])
def get_block_height():
    return jsonify({"block_height": 1})


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=80)
