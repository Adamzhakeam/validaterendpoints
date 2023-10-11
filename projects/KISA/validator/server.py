from flask import Flask,request,jsonify
from flask_cors import CORS
import threading
from api.validations.emailIsValid import isValid
from api.schema.digitsSchema import digitIsValid
from api.schema.stringSchema import stringIsValid
from api.validations.phoneNumberIsValid import isValid

app = Flask(__name__)
CORS(app)


@app.route("/validateEmail",methods=["POST"])
def validateEmail():
    data = request.json
    email = data.get('email','')
    isEmailValid = isValid(email)
    response = {
        'Is email Valid':isEmailValid
    }
    return jsonify(response)
    
@app.route('/validateFigures',methods=['POST'])
def validateFigures():
    data = request.json
    figure = data.get('figure',0)
    schema = data.get('schema','')
    isFigureValid = digitIsValid(figure,schema)
    response = {
        'Is Figure Valid':isFigureValid
    }
    return jsonify(response)  

@app.route('/validateString', methods=['POST'])
def validateString():
    data = request.json
    string = data.get('string',0)
    schema = data.get('schema','')
    isStringValid =  stringIsValid(string,schema)
    response = {
        'Is String Valid':isStringValid
    }
    return jsonify(response)

@app.route('/validatePhoneNumber',methods=['POST'])
def validatePhoneNumber():
    datae = request.json
    phoneNumber = datae.get('phoneNumber','')
    isPhoneNumberValid = isValid(phoneNumber)
    response = {
        'Is Phone Number Valid':isPhoneNumberValid
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True,threaded=True)