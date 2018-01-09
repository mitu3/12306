import requests
import re
import json

url ='https://kyfw.12306.cn/otn/leftTicket/queryZ?' \
     'leftTicketDTO.train_date=2018-01-19&' \
     'leftTicketDTO.from_station=BJP&' \
     'leftTicketDTO.to_station=TJP&purpose_codes=ADULT'
# cookies = {'_jc_save_fromStation':'%u5317%u4EAC%2CBJP',
#            '_jc_save_toStation':'%u5929%u6D25%2CTJP',
#            '_jc_save_fromDate':'2018-01-19'
#            }
#

req = requests.get(url)
# c = req.cookies
# cookdict = {c.name: c.value for c in req.cookies}
# print(c)
json_response = req.content.decode()  # 获取r的文本 就是一个json字符串

 # 将json字符串转换成dic字典对象
dict_json = json.loads(json_response)



raw_trains = (dict_json['data'])['result']
print(raw_trains)
print(len(raw_trains))

alldict = {}
for raw_train in raw_trains:
    # split切割之后得到的是一个列表
    data_list = raw_train.split("|")
    train_no = data_list[3].lower()

    print(data_list)
    print(train_no)
    # 判断是否是查询特定车次的信息
    # if not options or initial in options:
    from_station_code = data_list[6]
    to_station_code = data_list[7]
    from_station_name = ''
    to_station_name = ''
    start_time = data_list[8]
    arrive_time = data_list[9]
    time_duration = data_list[10]
    first_class_seat = data_list[31] or "--"
    second_class_seat = data_list[30] or "--"
    soft_sleep = data_list[23] or "--"
    hard_sleep = data_list[28] or "--"
    hard_seat = data_list[29] or "--"
    no_seat = data_list[33] or "--"
    ddd = data_list[12]
    zhong = [from_station_code,to_station_code,start_time,arrive_time,time_duration,first_class_seat,second_class_seat,
             soft_sleep,hard_sleep,hard_seat,no_seat,ddd]
    alldict[train_no] = zhong
    print(zhong)

#

# print(ddd)

