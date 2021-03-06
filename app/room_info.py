from flask import Blueprint, request, jsonify
from mysql import Room

room_info = Blueprint('room_info', __name__)

@room_info.route('', methods = ['GET'])
def RoomInfo(room_id):
    # 在数据库中查找教室信息
    record = Room.query.get(room_id)
    if record is None:
        return jsonify(error_code = -102, data = {})
    else:
        return jsonify(error_code = 0, data = {
                "id": record.room_id,
                "org": record.org,
                "picture": record.picture,
                "max_num": record.max_num,
                "description": record.description
            })