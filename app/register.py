import stu_apply_info
import room_use_info
import room_info
import stu_room_use
import room_floor_get
import time_get
import notice_list
import notice_info
import stu_apply


# 注册所有蓝本视图函数
def register_all(app):
    # http://xx.com/stu/apply/id
    # GET：我的申请详细内容
    # POST：修改申请内容
    app.register_blueprint(stu_apply_info.stu_apply_info, url_prefix='/api/stu/apply/<string:apply_id>')

    # http://xx.com/api/stu/room/use/id
    # GET: 教室使用说明
    app.register_blueprint(room_use_info.room_use_info, url_prefix='/api/stu/room/use/<string:room_id>')

    # http://xx.com/api/stu/room/id
    # GET: 查看教室介绍
    app.register_blueprint(room_info.room_info, url_prefix='/api/stu/room/<string:room_id>')

    # http://xx.com/stu/room/use
    # GET: 教室使用情况
    app.register_blueprint(stu_room_use.stu_room_use, url_prefix='/api/stu/room/use')

    # http://xx.com/api/stu/building
    # GET: 获取全部楼号
    app.register_blueprint(room_floor_get.room_floor_get, url_prefix='/api/stu/building')

    # http://xx.com/api/stu/timetable
    # GET: 获取时间表
    app.register_blueprint(time_get.time_get, url_prefix='/api/stu/timetable')
    
    # http://xx.com/api/stu/apply
    # POST: 学生提交教室申请
    app.register_blueprint(stu_apply.stu_apply, url_prefix='/api/stu/apply')

    # http://xx.com/api/stu/notice
    # GET: 查看公告列表
    app.register_blueprint(notice_list.notice_list, url_prefix='/api/stu/notice')

    # http://xx.com/api/stu/notice/id
    # GET: 查看公告详情
    app.register_blueprint(notice_info.notice_info, url_prefix='/api/stu/notice/<int:notice_id>')
