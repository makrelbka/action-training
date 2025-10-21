from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/count', methods=['POST'])
def count():
    phrase = request.json['phrase']
    result = "да" if len(phrase) > 10 else "нет"
    return jsonify({"result": result, "count": len(phrase)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)