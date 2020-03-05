# http://xx.com/stu/room/use

from flask import Blueprint, request, jsonify
from sqlalchemy import and_

from mysql import Apply, Room, Timetable
from app import db
import common

stu_room_use = Blueprint('stu_room_use', __name__)


# 创建一个原始的res_data
def create_res_data(rooms, timetable):
    res_data = dict()
    for room in rooms:
        floor = str(room.floor)
        if floor not in res_data:
            res_data[floor] = dict()

        res_data[floor][room.room_name] = dict(id=room.room_id, use=[True] * len(timetable))

    return res_data


# 将一个时间点对应到第几大节
def time_to_class(time, timetable, is_begin=True):
    if is_begin:
        for period in timetable:
            if period.begin_time <= time < period.end_time:
                return period.class_id
    else:
        for period in timetable:
            if period.begin_time < time <= period.end_time:
                return period.class_id
    return None


# 根据申请记录修改教室状态
def modify_room_status(room_status, record, timetable):
    begin_class = time_to_class(record.begin_time, timetable, is_begin=True)
    end_class = time_to_class(record.end_time, timetable, is_begin=False)
    for i in range(begin_class - 1, end_class):
        room_status[i] = False


# 根据申请记录修改 res_data
def modify_res_data(res_data, records, timetable):
    for record in records:
        cur_floor = res_data.get(str(record.floor))
        if cur_floor is None:
            continue
        room_status = cur_floor.get(record.room_name)
        if room_status is None:  # 说明所申请到的教室不在教室信息表中
            continue
        else:
            modify_room_status(room_status['use'], record, timetable)


# GET:查看教室使用情况
@stu_room_use.route('/')
def stu_room_use_info():
    # 解析json数据
    json_data = request.get_json(silent=True)
    if json_data is None:
        return jsonify(code=-101, data=None)

    # 检查json数据是否有缺少
    try:
        common.check_key(json_data, 'date', 'building')
    except KeyError:
        return jsonify(code=-101, data=None)

    # 获取时间表的信息
    timetable = Timetable.query.all()

    # 获取符合条件的全部教室 rooms 并生成初始化的结果数据 res_data
    building = json_data.get('building')
    rooms = Room.query.filter(and_(Room.building == building))
    # res_data = {room.room_name: [True] * len(timetable) for room in rooms}
    res_data = create_res_data(rooms, timetable)

    # 查询申请信息表中符合查询条件的申请记录
    records = Apply.query.filter(and_(Apply.check_status == "审核通过", Apply.use_date == json_data.get('date'),
                                      Apply.building == building)).all()

    # 根据申请记录修改 res_data
    modify_res_data(res_data, records, timetable)

    return jsonify(code=0, data=res_data)
