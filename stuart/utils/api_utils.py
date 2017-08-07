from datetime import datetime

from flask import jsonify


def json_response(**args):
    status_code = args['status']
    args.pop('status', None)
    response = jsonify({
        'datetime': datetime.now(),
        'status': status_code,
        'data': args,
    })
    return response, status_code

