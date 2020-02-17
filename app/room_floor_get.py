# http://xx.com/api/stu/building

from flask import Blueprint, jsonify
from mysql import Room

room_floor_get = Blueprint('room_number_get', __name__)


@room_floor_get.route('/', methods=['GET'])
def room_number_fun():
    room_list = Room.query.all()  # 获取Room表所有教室信息
    s = set()
    for i in room_list:
        s.add(i.building)
    assist_dict = {}
    room_data = []
    for i in s:
        assist_dict[i] = []
    for i in room_list:
        if i.floor not in assist_dict[i.building]:
            assist_dict[i.building].append(i.floor)
    for i in assist_dict:
        assist_dict[i].sort()
    sort = sorted(assist_dict)
    for i in sort:
        room_data.append({i: assist_dict[i]})
    return jsonify(code=0, data=room_data)