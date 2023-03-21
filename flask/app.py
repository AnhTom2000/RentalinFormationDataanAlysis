from flask import Flask, request, render_template, jsonify
import tools
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


# 时间
@app.route("/time")
def get_time():
    return tools.get_time()


# 返回center1数据
@app.route("/center1")
def get_center1_data():
    conn, db = tools.get_conn()
    # 获取数据库中的数据
    data = tools.get_center1_data()
    # 把数据转换为json字符串（安装simplejson,或者将取的数据强制转换为字符类型）
    return jsonify({"res": str(data[0]), "avg": str(int(data[1])), "min": str(data[2]), "area": str(data[3])})


# center2数据
@app.route("/center2")
def get_center2_data():
    res = []
    for i in tools.get_center2_data():
        res.append({"name": i["area1"], "value": int(i["unit_price"])})
    return jsonify({"data": res})


# left1数据
@app.route("/left1", methods=['get', 'post'])
def get_left1_data():
    data = tools.get_left1_data()
    day, avg = [], []
    for i in data:
        day.append((i['_id']))
        avg.append(i["avg_unit_price"])
    return jsonify({"day": day, "avg": avg})


# left2数据
@app.route("/left2", methods=['get', 'post'])
def get_left2_data():
    data = tools.get_left2_data()
    day, avg = [], []
    for i in data:
        day.append((i['_id']))
        avg.append(i["avg_unit_price"])

    return jsonify({"day": day, "avg": avg})


# left3数据
@app.route("/left3", methods=['get', 'post'])
def get_left3_data():
    data = tools.get_left3_data()
    d = []
    d.append({"value": data[0], "name": "有配备电梯"})
    d.append({"value": data[1], "name": "非共有产权"})
    d.append({"value": data[2], "name": "共有产权"})
    d.append({"value": data[4], "name": "精装"})
    d.append({"value": data[3], "name": "简装"})
    d.append({"value": data[5], "name": "未满两年"})
    d.append({"value": data[6], "name": "满两年"})
    d.append({"value": data[7], "name": "平层"})

    return jsonify({"data": d})


# right1数据
# @app.route("/right1", methods=['get', 'post'])
def get_right1_data():
    data = tools.get_right1_data()
    area, count = [], []
    for a, b in data:
        area.append(a)
        count.append(int(b))
    return jsonify({"area": area[0:10], "count": count[0:10]})


# @app.route("/right2", methods=['get', 'post'])
def get_right2_data():
    data = tools.get_right2_data()
    d = []
    for i in data:
        ks = extract_tags(i[0] + i[1] + i[2] + i[3] + i[4] + i[5] + i[6] + i[7] + i[8])
        for j in ks:
            if not j.isdigit():
                d.append({"name": j, "value": str(i[9])})
    return jsonify({"h": d})


if __name__ == '__main__':
    app.run()
