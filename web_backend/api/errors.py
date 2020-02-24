from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def bad_request(message):
    return error_response(400, message)


def good_request(message):
    return error_response(201, message, label='info', error='')


def error_response(status_code, message=None, label='error', error='Unknown error'):
    payload = {label: HTTP_STATUS_CODES.get(status_code, error)}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response
