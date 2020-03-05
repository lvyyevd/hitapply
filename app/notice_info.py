from flask import Blueprint, request, jsonify

from mysql import Notice
from common import turn_to_string


notice_info = Blueprint('notice_info', __name__)
@notice_info.route('', methods = ['GET'])

def notice_info(notice_id):
    record = Notice.query.get(notice_id)

    if record is None:
        return jsonify(error_code = -102, data = {})

     data = {
            'id': record.notice_id,
            'title': record.org,
            'time': turn_to_string(record.time)
            "content": record.content
        }
    return jsonify(code=0, data=data)