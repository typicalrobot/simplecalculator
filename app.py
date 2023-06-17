from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    operation = request.form.get('operation')

    if operation == 'add':
        result = float(num1) + float(num2)
    elif operation == 'subtract':
        result = float(num1) - float(num2)
    elif operation == 'multiply':
        result = float(num1) * float(num2)
    elif operation == 'divide':
        result = float(num1) / float(num2)

    return render_template('home.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
