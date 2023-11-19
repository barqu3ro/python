from flask import Flask, request

app = Flask(__name__)

@app.route('/verify', methods=['GET'])
def verify_number():
    number = request.args.get('number', default = 1, type = int)
    result = verificarNumeroSheldon(number)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)