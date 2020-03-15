# http://xx.com/api/stu/building

from flask import Blueprint, jsonify
from mysql import Room

room_floor_get = Blueprint('room_number_get', __name__)


@room_floor_get.route('/', methods=['GET'])
def room_number_fun():
    room_list = Room.query.all()  # 获取Room表所有教室信息
    s = set()   # s是楼的集合
    dic = {}    # 用dic辅助对列表进行排序，因为两层字典内的列表无法使用sort()排序
    for i in room_list:
        s.add(i.building)
    room_data = {}
    for i in s:
        room_data[i] = {}
    for i in room_list:
        if i.building+'*&'+str(i.floor) not in dic:
            dic[i.building+'*&'+str(i.floor)] = []
        dic[i.building+'*&'+str(i.floor)].append(i.room_name)
    for i in dic:
        dic[i].sort()
        pre_suf = str(i).split('*&')
        pre = pre_suf[0]
        suf = pre_suf[1]
        room_data[pre][suf] = dic[i]
    return jsonify(code=0, data=room_data)