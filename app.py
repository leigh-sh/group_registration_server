import logging
import os
from datetime import datetime

from flask import Flask, request, Response

app = Flask(__name__)

logging.getLogger('').setLevel(os.getenv("LOGGING_LEVEL", logging.DEBUG))


@app.route('/createMember', methods=['POST'])
def create_member():
    data = request.get_json() or {}
    member_email = data['email']
    created_at = datetime.now()
    # approved_at = datetime.now()
    # approved (bool)
    referrer = data['referrer']

    # db post: email, referee, createdAt, approved [yes/no], approvedAt

    return Response(status=200, mimetype='application/json')


@app.route('/health', methods=['GET'])
def health_check():
    return Response('hooray', status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()