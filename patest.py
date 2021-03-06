import requests



url = 'https://kyfw.12306.cn/otn/leftTicket/init'
cookies = {'_jc_save_fromStation':'%u5317%u4EAC%2CBJP',
           '_jc_save_toStation':'%u5929%u6D25%2CTJP',
           '_jc_save_fromDate':'2018-01-09'
           }

x = requests.post(url,  cookies=cookies)
c = x.cookies
print(x.cookies)
print ({c.name: c.value for c in x.cookies})
# coding: utf-8

# """命令行火车票查看器:Usage　Options为docopt库固定格式
#
# Usage:
#     tickets [-dgktz] <from> <to> <date>
#
# Options:
#     -h, --help 查看帮助
#     -d         动车
#     -g         高铁
#     -k         快速
#     -t         特快
#     -z         直达
#
# Examples:
#     tickets 上海 北京 2017-10-10
#     tickets -dg 成都 南京 2017-10-10
# """
#
# from docopt import docopt
# import requests
# from prettytable import PrettyTable
# from colorama import Fore
# import stations
#
#
# def cli():
#     arguments = docopt(__doc__, version='ticket 1.0')
#     from_station = stations.get_telecode(arguments.get('%u5317%u4EAC%2CBJP'))
#     to_station = stations.get_telecode(arguments.get('%u5929%u6D25%2CTJP'))
#     date = arguments.get('2018-01-09')
#     # 列表推导式，得到的是查询车次类型的集合
#     options = ''.join([key for key, value in arguments.items() if value is True])
#     print(options)
#
#     url = ('https://kyfw.12306.cn/otn/leftTicket/query?'
#            'leftTicketDTO.train_date={}&'
#            'leftTicketDTO.from_station={}&'
#            'leftTicketDTO.to_station={}&'
#            'purpose_codes=ADULT').format(date, from_station, to_station)
#
#     r = requests.get(url, verify=False)
#     # print(r.json())
#     # 　　requests得到的是一个json格式的对象，ｒ.json()转化成python字典格式数据来提取，所有的车次结果result
#     raw_trains = r.json()['data']['result']
#     pt = PrettyTable()q
#     pt._set_field_names("车次　车站　时间　经历时　一等座　二等座　软卧　硬卧 硬座　无座".split())
#     for raw_train in raw_trains:
#         # split切割之后得到的是一个列表
#         data_list = raw_train.split("|")
#         train_no = data_list[3]
#         initial = train_no[0].lower()
#         # print(train_no[0])
#         # 判断是否是查询特定车次的信息
#         if not options or initial in options:
#             from_station_code = data_list[6]
#             to_station_code = data_list[7]
#             from_station_name = ''
#             to_station_name = ''
#             start_time = data_list[8]
#             arrive_time = data_list[9]
#             time_duration = data_list[10]
#             first_class_seat = data_list[31] or "--"
#             second_class_seat = data_list[30] or "--"
#             soft_sleep = data_list[23] or "--"
#             hard_sleep = data_list[28] or "--"
#             hard_seat = data_list[29] or "--"
#             no_seat = data_list[33] or "--"
#
#         pt.add_row([
#             # 对特定文字添加颜色
#             train_no,
#             '\n'.join([Fore.GREEN + stations.get_name(from_station_code) + Fore.RESET,
#                        Fore.RED + stations.get_name(to_station_code) + Fore.RESET]),
#             '\n'.join([Fore.GREEN + start_time + Fore.RESET, Fore.RED + arrive_time + Fore.RESET]),
#             time_duration,
#             first_class_seat,
#             second_class_seat,
#             soft_sleep,
#             hard_sleep,
#             hard_seat,
#             no_seat
#         ])
#
#     print(pt)
#
#
# if __name__ == '__main__':
#     cli()