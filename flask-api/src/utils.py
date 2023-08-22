import json
from flask import Response


def json_response(message, status=200, headers=None):
    msg = json.dumps(message)
    resp = Response(
        status=status,
        response=msg,
        headers=headers,
        mimetype="application/json")
    return resp
