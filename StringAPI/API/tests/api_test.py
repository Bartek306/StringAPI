import json

import requests


def invalid_response_test():
    request = requests.post("http://localhost:8000/string")
    assert request.status_code == 404


def valid_response_test():
    message = 'teSt_message'
    data = {'message': message}
    data = json.dumps(data)
    request = requests.post("http://localhost:8000/string", data)
    assert request.status_code == 200
    dict = request.text
    dict = json.loads(dict)
    assert dict['lower'] == 10
    assert dict['special'] == 1
    assert dict['upper'] == 1


def test():
    invalid_response_test()
    valid_response_test()

test()
