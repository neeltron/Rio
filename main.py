from flask import Flask, jsonify
app = Flask('app')

mode = "w"

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/drive', methods = ['GET'])
def drive():
  return jsonify(mode)

app.run(host='0.0.0.0', port=8080)
