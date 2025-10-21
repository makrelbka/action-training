from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phrase = request.form['phrase']
        try:
            response = requests.post('http://back:5001/count', json={'phrase': phrase})
            data = response.json()
            return render_template('index.html', result=data['result'], count=data['count'])
        except:
            return render_template('index.html', error="Бекенд недоступен")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)