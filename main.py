from flask import Flask, jsonify, request, render_template
from replit import db

app = Flask('app', template_folder = "templates", static_folder = "static")

mode = ""

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/drive', methods = ['GET'])
def drive():
  return jsonify(db["direction"])

@app.route('/control', methods = ['GET'])
def control():
  mode = request.args.get('dir')
  db["direction"] = mode
  return render_template('index.html')

app.run(host='0.0.0.0', port=8080)
