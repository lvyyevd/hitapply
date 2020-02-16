# http://xx.com/api/stu/timetable

from flask import Blueprint, jsonify
from mysql import Timetable
from common import turn_to_string

time_get = Blueprint('time_get', __name__)

int_to_class = {1: '第一节', 2: '第二节', 3: '第三节', 4: '第四节', 5: '第五节', 6: '第六节',
                7: '第七节', 8: '第八节', 9: '第九节'}


@time_get.route('/', methods=['GET'])
def get_timetable():
    Time = Timetable.query.all()  # 获取所有时间信息
    data_time = []
    for i in Time:
        data_time.append([int_to_class[i.class_id], turn_to_string(i.begin_time), turn_to_string(i.end_time)])
    return jsonify(code=0, data=data_time)