from flask import Flask, jsonify, request, render_template
app = Flask('app', template_folder = "templates", static_folder = "static")

mode = "w"

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/drive', methods = ['GET'])
def drive():
  return jsonify(mode)

@app.route('/control', methods = ['GET'])
def control():
  move = request.args.get('dir')
  print(move)
  return render_template('index.html')

app.run(host='0.0.0.0', port=8080)
