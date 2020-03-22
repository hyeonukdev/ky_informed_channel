from datetime import datetime
import json
from collections import OrderedDict

with open('food_foodmenu.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

month = datetime.today().month      # 현재 월 가져오기
day = datetime.today().day      # 현재 일 가져오기
date = str(month) + "월 " + str(day) + "일"

campus1 = json_data["죽헌정보관"]
today_campus1_menu = campus1[date]
today_campus1_menu_breakfast = "\n".join(today_campus1_menu["아침"])
today_campus1_menu_lunch = "\n".join(today_campus1_menu["점심"])
today_campus1_menu_dinner = "\n".join(today_campus1_menu["저녁"])
campus2 = json_data["건양회관"]
today_campus2_menu = campus2[date]
today_campus2_menu_breakfast = "\n".join(today_campus2_menu["아침"])
today_campus2_menu_lunch = "\n".join(today_campus2_menu["점심"])
today_campus2_menu_dinner = "\n".join(today_campus2_menu["저녁"])

data1 = OrderedDict()
data2 = OrderedDict()
file_data = OrderedDict()
data1["아침"] = today_campus1_menu_breakfast
data1["점심"] = today_campus1_menu_lunch
data1["저녁"] = today_campus1_menu_dinner
file_data["죽헌정보관"] = data1
data2["아침"] = today_campus1_menu_breakfast
data2["점심"] = today_campus1_menu_lunch
data2["저녁"] = today_campus1_menu_dinner
file_data["건양회관"] = data2

with open('food_foodmenu_today.json', 'w', encoding='utf-8') as make_file:
    json.dump(file_data, make_file, ensure_ascii=False)