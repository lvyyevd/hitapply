# http://xx.com/api/stu/building

from flask import Blueprint, jsonify
from mysql import Room

room_floor_get = Blueprint('room_number_get', __name__)


@room_floor_get.route('/', methods=['GET'])
def room_number_fun():
    room_list = Room.query.all()  # 获取Room表所有教室信息
    # 楼层转换
    turn_num = {-1: '负一楼', -2: '负二楼', -3: '负三楼 ', -4: '负四楼', -5: '负五楼', 1: '一楼',
                2: '二楼', 3: '三楼', 4: '四楼', 5: '五楼', 6: '六楼', 7: '七楼', 8: '八楼', 9: '九楼',
                10: '十楼', 11: '十一楼', 12: '十二楼', 13: '十三楼', 14: '十四楼', 15: '十五楼 '}
    s = set()
    for i in room_list:
        s.add(i.building)
    assist_dict = {}
    room_data = []
    for i in s:
        assist_dict[i] = []
    for i in room_list:
        if turn_num[i.floor] not in assist_dict[i.building]:
            assist_dict[i.building].append(turn_num[i.floor])
    for i in assist_dict:
        assist_dict[i].sort()
    sort = sorted(assist_dict)
    for i in sort:
        room_data.append({'name': i, 'floor': assist_dict[i]})
    return jsonify(code=0, data=room_data)