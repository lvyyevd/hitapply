import stu_apply_info

# 注册所有蓝本视图函数
def register_all(app):
	# http://xx.com/stu/apply/id
	# GET：我的申请详细内容
	# POST：修改申请内容
	app.register_blueprint(stu_apply_info.stu_apply_info, url_prefix='/stu/apply/<string:apply_id>')