from flask import Blueprint, request, jsonify
from mysql import Notice
from common import turn_to_string


notice_list = Blueprint('notice_list', __name__)
@notice_list.route('', methods = ['GET'])

def Notice_List():
    data = []
    record = Notice.query.all().order_by(Notice.time)

    if record is None:
        return jsonify(error_code = -102, data = {})

    for i in record:
        temp = {
            'id': i.notice_id,
            'title': i.org,
            'time': turn_to_string(i.time)
        }
        data.append(temp)
    return jsonify(code=0, data=data)
