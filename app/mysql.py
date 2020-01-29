# 数据库模型文件

from app import db


# 管理员账号信息表
class Administrator(db.Model):
    account = db.Column(db.String, primary_key=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    grade = db.Column(db.SmallInteger, nullable=False)
    name = db.Column(db.String)
    org = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)


# 公告信息表
class Notice(db.Model):
    notice_id = db.Column(db.String, primary_key=True, nullable=False)
    org = db.Column(db.String, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)


# 教室信息表
class Room(db.Model):
    room_num = db.Column(db.String, primary_key=True, nullable=False)
    org = db.Column(db.String, nullable=False)
    picture = db.Column(db.String)
    max_num = db.Column(db.Integer, nullable=False)
    permissible = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.Text)


# 预约信息表
class Apply(db.Model):
    apply_id = db.Column(db.String, primary_key=True, nullable=False)
    activity_name = db.Column(db.String, nullable=False)
    applicant_id = db.Column(db.String, nullable=False)
    applicant_name = db.Column(db.String, nullable=False)
    applicant_phone = db.Column(db.String, nullable=False)
    apply_time = db.Column(db.DateTime, nullable=False)
    begin_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    people_count = db.Column(db.Integer, nullable=False)
    request = db.Column(db.Text)
    org = db.Column(db.String)
    teacher_name = db.Column(db.String, nullable=False)
    material = db.Column(db.String)
    check_status = db.Column(db.Enum('待审核', '审核通过', '审核失败'), nullable=False)
    note = db.Column(db.Text)
    verifier_name = db.Column(db.String)
    room_num = db.Column(db.String, nullable=False, default='不指定')
