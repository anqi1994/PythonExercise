from flask import Flask, jsonify

app = Flask(__name__)


def calculate_prime(number):
    if number <= 2:
        return False
    for i in range(2, int(number)):
        if number % i == 0:
            return False
    return True


@app.route('/prim_number/<int:number>', methods=['GET'])
def check_prime_number(number):
    result = {
        "Number": number,
        "calculatePrime": calculate_prime(number)
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
