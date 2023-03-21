import time
import pymysql
import pymongo
from pymongo.collation import Collation


# 获取时间
def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年", "月", "日")


def get_conn():
    # 连接数据库服务器 ↓
    conn = pymongo.MongoClient('mongodb://admin:7355608@1.15.116.64:27018/?authSource=admin')
    # 选择数据库 ↓
    db_housedatabase = conn["housedatabase"]  # 推荐使用：db_test = client["test"]
    # 获取集合 ↓
    shenzhen = db_housedatabase["shenzhen"]
    return conn, shenzhen


def close_conn(conn):
    conn.close()


def query(msql, *args):
    # args是占位符
    conn, db = get_conn()
    # 根据条件查找文档并格式化
    res = db.find(msql)
    return res


def get_center1_data():
    conn, db = get_conn()
    res = []
    getcount = db.aggregate([{'$group': {'_id': None, 'count': {'$sum': 1}}}])
    getmin = db.find().sort('unit_price', 1).collation(Collation(locale='zh', numericOrdering=True)).limit(1)
    getavg = db.aggregate([
        {'$group': {'_id': '$listing_time', 'avg_unit_price': {'$avg': {'$toDouble': '$unit_price'}}},
         }])
    for i in getcount:
        res.append(i["count"])
    for i in getavg:
        res.append(i["avg_unit_price"])
        break
    for i in getmin:
        res.append(i["unit_price"])
        res.append(i["area1"])
    return res


def get_center2_data():
    conn, db = get_conn()
    res = db.find()
    return res


def get_left1_data():
    conn, db = get_conn()
    res = db.aggregate([
        {'$group': {'_id': '$listing_time', 'avg_unit_price': {'$avg': {'$toDouble': '$unit_price'}}}},
        {'$sort': {'listing_time': 1}}])

    # res = db.find({'unit_price': 1}, {'listing_time': 1}).sort("listing_time", pymongo.DESCENDING)
    # sql = "SELECT `yearMontthTime`," \
    #       "`avg_unit_price` " \
    #       "FROM `ADS_house_YearMonthAvgUnitPrice` " \
    #       "GROUP BY `yearMontthTime`"
    # res = query(sql)
    return res


def get_left2_data():
    conn, db = get_conn()
    res = db.aggregate([
        {'$group': {'_id': '$listing_time', 'avg_unit_price': {'$avg': {'$toDouble': '$unit_price'}}}},
        {'$sort': {'listing_time': 1}}]
    )
    # sql = "SELECT `yearMontthTime`," \
    #       "`dayTime`," \
    #       "`avg_unit_price` " \
    #       "FROM `ADS_house_YearMonthAvgUnitPrice` " \
    #       "GROUP BY `yearMontthTime`,`dayTime`"
    # res = query(sql)
    return res


def get_left3_data():
    conn, db = get_conn()
    elevator = db.find({'elevator': '有'})
    property_ownership1 = db.find({'property_ownership' : '非共有'})
    property_ownership2 = db.find({'property_ownership' : '共有'})
    decoration1 = db.find({'decoration' : '简装'})
    decoration2 = db.find({'decoration' : '精装'})
    service_life1 = db.find({'service_life' : '未满两年'})
    service_life2 = db.find({'service_life' : '满两年'})
    apartment_structure = db.find({'apartment_structure' : '平层'})

    res = []
    count = 0
    for i in elevator:
        count += 1
    res.append(count)

    count = 0
    for i in property_ownership1:
        count += 1
    res.append(count)

    count = 0

    for i in property_ownership2:
        count += 1
    res.append(count)
    count = 0
    for i in decoration1:
        count += 1
    res.append(count)
    count = 0
    for i in decoration2:
        count += 1
    res.append(count)
    count = 0
    for i in service_life1:
        count += 1
    res.append(count)
    count = 0
    for i in service_life2:
        count += 1
    res.append(count)
    count = 0
    for i in apartment_structure:
        count += 1
    res.append(count)

    # sql = "SELECT round((SELECT count(`lift`) FROM `DWD_house` WHERE `lift`='有')/count(*),2)," \
    #       "round((SELECT count(`usright`) FROM `DWD_house` WHERE `usright`='非共有')/count(*),2)," \
    #       "round((SELECT count(`usright`) FROM `DWD_house` WHERE `usright`='共有')/count(*),2)," \
    #       "round((SELECT count(`decorate`) FROM `DWD_house` WHERE `decorate`='精装')/count(*),2)," \
    #       "round((SELECT count(`decorate`) FROM `DWD_house` WHERE `decorate`='简装')/count(*),2)," \
    #       "round((SELECT count(`usyear`) FROM `DWD_house` WHERE `usyear`='未满两年')/count(*),2)," \
    #       "round((SELECT count(`usyear`) FROM `DWD_house` WHERE `usyear`='满五年')/count(*),2)," \
    #       "round((SELECT count(`structure`) FROM `DWD_house` WHERE `structure`='平层')/count(*),2)" \
    #       "FROM `DWD_house` "
    # res = query(sql)
    return res


def get_right1_data():
    conn, db = get_conn()
    res = db.aggregate([
        {
            '$group': {'_id': '$area1', 'num': {'$sum': 1}}
        },
        {
            '$sort': {'num': {'$sum': 1}
                      }
        }]
    )
    # sql = "SELECT `lodge_reion`," \
    #       "count(*) as num " \
    #       "FROM `DWD_house` " \
    #       "GROUP BY `lodge_reion` " \
    #       "ORDER BY num desc"
    # res = query(sql)
    return res


def get_right2_data():
    conn, db = get_conn()
    res = db.aggregate([{'$group': {"_id": "$_id"}}, {'$sort': {'_id': 1}}])
    # sql = "SELECT `floors`,`building_structure`," \
    #       "`building_type`,`decorate`,`ladder`,`ownership`," \
    #       "`usages`,`usyear`,`building_head`,`ID` " \
    #       "FROM `DWD_house` GROUP BY `ID` ORDER BY `ID`"
    #
    # res = query(sql)
    return res


if __name__ == '__main__':
    pass
