from flask import Blueprint, request, jsonify

from mysql import Notice
from common import turn_to_string


notice_info = Blueprint('notice_info', __name__)
@notice_info.route('', methods = ['GET'])

def notice_info(notice_id):
    if notice_id == -1:
        length = len(Notice.query.all())
        record = Notice.query.get(length)
        if record is None:
            return jsonify(code=-102, data={})
        else:
            data = {
                'id': record.notice_id,
                'title': record.org,
                'time': turn_to_string(record.time),
                "content": record.content
            }
            return jsonify(code=0, data=data)
    else:
        record = Notice.query.get(notice_id)
        if record is None:
            return jsonify(code = -102, data = {})
        else:
            data = {
                'id': record.notice_id,
                'title': record.org,
                'time': turn_to_string(record.time),
                "content": record.content
            }
            return jsonify(code=0, data=data)
