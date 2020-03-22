from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
import json
from collections import OrderedDict

auto_schedule = OrderedDict()

html = requests.get(
    'https://www.konyang.ac.kr/prog/schedule/kor/sub06_01_01_01/3/haksa.do')
soup = bs(html.text, 'html.parser')

schedule_title = soup.select('div.schdule_title > p')[0].text
# print("------년도가져오기-----")
# print(schedule_title)
# print("-----------")
schedule = soup.select('table > tbody > tr')[1]
# print(schedule)
# print("------목록가져오기-----")
schedule_month_list = []
schedule_day_list = []
schedule_work_list = []
for i in range(25):
    try:
        schedule_month = soup.select('table > tbody > tr')[
            i].select('th')[0].text
    except:
        schedule_month = schedule_month_list[-1]
        schedule_month_list.append(schedule_month)
        auto_schedule["schedule_month"] = schedule_month
    else:
        schedule_month_list.append(schedule_month)
        auto_schedule["schedule_month"] = schedule_month

    schedule_day = soup.select('table > tbody > tr')[i].select('td')[0].text
    schedule_day_list.append(schedule_day)
    auto_schedule["schedule_day"] = schedule_day
    schedule_work = soup.select('table > tbody > tr')[i].select('td')[1].text
    schedule_work_list.append(schedule_work)
    auto_schedule["schedule_work"] = schedule_work

# print(schedule_month_list)
# print(schedule_day_list)
# print(schedule_work_list)
result = []
make_dictionary = [schedule_day_list, schedule_work_list]
for i, j in zip(schedule_day_list, schedule_work_list):
    result.append(i+" "+j)

newDict = dict()
print(schedule_month_list[0]+result[0])
print(schedule_month_list[1]+result[1])

dic = {name: value for name, value in zip(schedule_month_list, result)}
print(dic)

# print(json.dumps(newDict, ensure_ascii=False))

# with open('../json/admin_schedule.json', 'w', encoding='utf-8') as make_file:
#     json.dump(newDict, make_file, ensure_ascii=False)
