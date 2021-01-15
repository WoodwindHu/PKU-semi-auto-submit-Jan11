import json

config = {}
config["学号"] = "123123"
config["密码"] = "123123"

config["出入校起点"] = "畅春园" # 燕园 校外 ... 暂不支持校外
config["出入校终点"] = "燕园" # 燕园 校外 ...
config["起点/终点校门"] = "西南门" # 畅春园新门 东南门 南门 西门 校医院便民通道 小东门 东侧门 东门 西南门 燕园大厦门
config["出入校事由"] = "科研" # 就业 就学 科研 就医
config["出入校具体事项"] = "递交材料、食堂就餐" # 200字
config["起点/终点所在国家地区"] = "中国" # 中国 ...
config["起点/终点所在省"] = "北京市" # 北京市 ...
config["起点/终点所在地级市"] = "市辖区" # 市辖区 其他
config["起点/终点所在区县"] = "海淀区" # 海淀区 ...
config["起点/终点所在街道"] = "海淀街道" # 100字
config["基本轨迹"] = "西南门进，到新太阳交材料，食堂就餐，西南门出" # 200字
config["补充说明"] = "暂无" # 200字
config["证明材料上传"] = "北京健康宝" # 网页支持多个，这里自动点击一个，其余的需要手动增加
config["邮箱"] = "123123@qq.com"
config["手机号"] = "123123"
config["宿舍园区"] = ""
config["宿舍楼"] = ""
config["宿舍房间号"] = ""
config["程序暂停"] = "否"
config["提交"] = "是"
config["微信通知key"] = ""

with open("config-example.json", "w", encoding="utf-8") as f1:
    json.dump(config, f1, ensure_ascii=False, indent=4)
