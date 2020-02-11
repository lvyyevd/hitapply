# 公共函数文件

# 检查一个字典中是否有一系列的key
def check_key(aDict, *keys):
    for k in keys:
        if k in aDict:  # 存在该键
            continue
        else:  # 不存在该键，抛出KeyError异常
            raise KeyError
