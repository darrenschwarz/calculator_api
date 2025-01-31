from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = num1 + num2
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400
    
@app.route('/subtract', methods=['GET'])
def subtract():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = num1 + num2  # Intentional bug: should be subtraction update
        return jsonify({'result': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400


if __name__ == '__main__':
    app.run(debug=True)
