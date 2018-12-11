from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)

CORS(app)

@app.route('/hello')
def sayHello():
    greetingList = ['Ciao', 'Hei', 'Salut', 'Hola', 'Hallo', 'Hej']
    return random.choice(greetingList)



if __name__ == '__main__':
    app.run(debug=True)