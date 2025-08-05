from flask import Flask, request, jsonify

app = Flask(__name__)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

@app.route('/suma', methods=['POST'])
def suma_endpoint():
    data = request.get_json()
    a, b = data['a'], data['b']
    return jsonify({'result': suma(a, b)})

@app.route('/resta', methods=['POST'])
def resta_endpoint():
    data = request.get_json()
    a, b = data['a'], data['b']
    return jsonify({'result': resta(a, b)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)